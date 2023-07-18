import csv
import os
import datetime
from tabulate import tabulate
#-*- coding: utf-8 -*-
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#-----------------------------Funciones de menu-----------------
def main_menu():
    clear_screen()
    print("=== Menú Principal ===")
    print("1. Realizar pedido")
    print("2. Realizar devoluciones")
    print("3. Calcular volumen")
    print("4. Ingresar productos")
    print("5. Mostrar productos")
    print("6. Eliminar Productos")
    print("7. Mostrar Pedidos")
    print("8. Salir")

def submenu():
    input("Presiona Enter para volver al Menú Principal.")

#--------------------------Manejo de productos------------------

def ingresar_productos():
    clear_screen()
    print("Estás en la opción 'Ingresar productos'")

    while True:
        try:
            nombre = input("Nombre: ")
            tamaño = float(input("Tamaño: "))
            cantidadUni = int(input("Cant. uni. x bulto:"))

            producto = {
                "Nombre": nombre,
                "Tamaño": tamaño,
                "CantidadUni": cantidadUni
            }

            productos.append(producto)
            print("Producto ingresado exitosamente.")

            respuesta = input("¿Deseas ingresar otro producto? (si/no): ")
            if respuesta.lower() != "si":
                guardar_en_csv()
                break

        except ValueError:
            print("Dato incorrecto. Por favor, ingresa el dato correctamente.")

    submenu()

def eliminar_producto():
    while True:
        clear_screen()
        print("=== Eliminar Producto ===")
        mostrar_productos()
        
        productos = []
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            encabezados = next(lector_csv)  # Ignorar la primera fila (encabezados)
            for fila in lector_csv:
                productos.append(fila)

        if not productos:
            print("No hay productos para eliminar.")
            break

        num_producto = input("Ingresa el número del producto que deseas eliminar (0 para cancelar): ")
        if num_producto == "0":
            break

        try:
            num_producto = int(num_producto)
            if num_producto < 1 or num_producto > len(productos):
                print("Número de producto inválido.")
            else:
                del productos[num_producto - 1]
                with open(archivo_csv, 'w', newline='') as archivo:
                    escritor_csv = csv.writer(archivo)
                    escritor_csv.writerow(encabezados)
                    escritor_csv.writerows(productos)
                print("Producto eliminado exitosamente.")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

        opcion = input("¿Deseas eliminar otro producto? (si/no): ")
        if opcion.lower() != "si":
            break

def mostrar_productos():
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Leer la primera fila como encabezados
        
        # Imprimir los encabezados con ajuste de anchura
        for encabezado in encabezados:
            print(encabezado.ljust(15), end='')
        print()
        
        # Imprimir las filas numeradas
        for i, fila in enumerate(lector_csv, start=1):
            print(str(i).ljust(3), end='')  # Imprimir el número de fila
            
            # Imprimir cada valor de la fila con ajuste de anchura
            for valor in fila:
                print(valor.ljust(15), end='')
            print()
    
    input("Presiona Enter para continuar...")



productos = []
archivo_csv = 'productos.csv'


#------------------------------Manejo de archivos-----------------------------

def guardar_en_csv():
    with open(archivo_csv, 'w', newline='') as archivo:
        campos = ['Nombre', 'Tamaño', 'CantidadUni']
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

        escritor_csv.writeheader()
        for producto in productos:
            escritor_csv.writerow(producto)

def obtener_archivos_pedidos():
    archivos_pedidos = []

    if not os.path.exists('pedidos.csv'):
        return archivos_pedidos

    with open('pedidos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            archivos_pedidos.append(fila[2])

    return archivos_pedidos

def mostrar_contenido_archivo(nombre_archivo):
    productos = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Ignorar la primera fila (encabezados)
        for fila in lector_csv:
            productos.append(fila)

    if not productos:
        print("El archivo está vacío.")
        return

    # Agregar encabezados a la lista de productos
    productos.insert(0, encabezados)

    # Imprimir los contenidos centrados
    print(tabulate(productos, headers="firstrow", tablefmt="center"))


def obtener_fecha_actual():
    fecha_actual = datetime.date.today()
    return fecha_actual.strftime("%Y-%m-%d")



#------------------------Calculo de volumen----------------------------------


def calcular_volumen():
    clear_screen()
    print("=== Calcular Volumen ===")
    clear_screen()
    print("=== Listado de Pedidos ===")

    if not os.path.exists('pedidos.csv'):
        print("No hay pedidos registrados.")
        submenu()
        return

    with open('pedidos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        pedidos = list(lector_csv)

    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        submenu()
        return

    for i, pedido in enumerate(pedidos):
        print(f"{i + 1}. Número de Pedido: {pedido[0]}")
        print(f"   Fecha: {pedido[1]}")
        print(f"   Archivo: {pedido[2]}")
        print()

    if not os.path.exists('pedidos.csv'):
        print("No hay pedidos registrados.")
        submenu()
        return

    with open('pedidos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        pedidos = list(lector_csv)

    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        submenu()
        return

    num_pedido = input("Selecciona el número de pedido para calcular el volumen (0 para cancelar): ")
    if num_pedido == "0":
        submenu()
        return

    try:
        num_pedido = int(num_pedido)
        if num_pedido < 1 or num_pedido > len(pedidos):
            print("Número de pedido inválido.")
            submenu()
            return

        nombre_archivo = pedidos[num_pedido - 1][2]
        productos = []
        with open(nombre_archivo, 'r') as archivo_pedido:
            lector_csv = csv.DictReader(archivo_pedido)
            for producto in lector_csv:
                cantidad_unidades = int(producto['CantidadUni'])
                cantidad_bultos = int(producto['CantidadBultos'])
                tamaño = float(producto['Tamaño'])
                volumen = cantidad_unidades * cantidad_bultos * tamaño
                producto['Volumen'] = volumen
                productos.append(producto)

        if not productos:
            print("El pedido está vacío.")
            submenu()
            return

        # Calcular la suma de los volúmenes de todos los productos del pedido
        volumen_total = sum(producto['Volumen'] for producto in productos)

        # Agregar fila vacía con la suma de los volúmenes al final de la lista de productos
        productos.append({'Volumen': volumen_total})

        # Mostrar los productos con el campo de volumen
        print(tabulate(productos, headers='keys', tablefmt='fancy_grid'))

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número de pedido válido.")

    submenu()

   
#--------------------------------Manejo de pedidos-----------------------------

def realizar_pedido():
    clear_screen()
    print("=== Realizar Pedido ===")
    mostrar_productos()

    productos = []
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Ignorar la primera fila (encabezados)
        for fila in lector_csv:
            productos.append(fila)

    if not productos:
        print("No hay productos disponibles para realizar un pedido.")
        submenu()
        return

    pedido = []
    numero_pedido = obtener_numero_pedido()
    fecha_pedido = obtener_fecha_actual()

    while True:
        num_producto = input("Ingresa el número del producto que deseas incluir en el pedido (0 para terminar): ")
        if num_producto == "0":
            break

        try:
            num_producto = int(num_producto)
            if num_producto < 1 or num_producto > len(productos):
                print("Número de producto inválido.")
                continue

            cantidad_bultos = input("Ingresa la cantidad de bultos del producto: ")
            try:
                cantidad_bultos = int(cantidad_bultos)
                if cantidad_bultos < 1:
                    print("La cantidad de bultos debe ser mayor a cero.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero válido.")
                continue

            producto_seleccionado = productos[num_producto - 1]
            producto_pedido = {
                "Nombre": producto_seleccionado[0],
                "Tamaño": float(producto_seleccionado[1]),
                "CantidadUni": int(producto_seleccionado[2]),
                "CantidadBultos": cantidad_bultos,
                "NumeroPedido": numero_pedido
            }
            pedido.append(producto_pedido)

            print("Producto agregado al pedido.")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número de producto válido.")

    if not pedido:
        print("El pedido está vacío.")
        submenu()
        return

    guardar_pedido(pedido, fecha_pedido, numero_pedido)
    print("Pedido realizado con éxito.")

    submenu()

def obtener_numero_pedido():
    # Verificar si el archivo de pedidos existe
    if not os.path.exists('pedidos.csv'):
        return 1

    # Leer el archivo de pedidos y obtener el último número de pedido
    with open('pedidos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            pass

        ultimo_numero_pedido = int(fila[0])

    # Incrementar el último número de pedido en 1 para el nuevo pedido
    nuevo_numero_pedido = ultimo_numero_pedido + 1

    return nuevo_numero_pedido

def mostrar_pedidos():
    clear_screen()
    print("=== Listado de Pedidos ===")

    if not os.path.exists('pedidos.csv'):
        print("No hay pedidos registrados.")
        submenu()
        return

    with open('pedidos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        pedidos = list(lector_csv)

    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        submenu()
        return

    for i, pedido in enumerate(pedidos):
        print(f"{i + 1}. Número de Pedido: {pedido[0]}")
        print(f"   Fecha: {pedido[1]}")
        print(f"   Archivo: {pedido[2]}")
        print()

    num_pedido = input("Selecciona el número de pedido para mostrar su contenido (0 para cancelar): ")
    if num_pedido == "0":
        submenu()
        return

    try:
        num_pedido = int(num_pedido)
        if num_pedido < 1 or num_pedido > len(pedidos):
            print("Número de pedido inválido.")
            submenu()
            return

        nombre_archivo = pedidos[num_pedido - 1][2]
        mostrar_contenido_archivo(nombre_archivo)

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número de pedido válido.")

    submenu()

def guardar_pedido(pedido, fecha_pedido, numero_pedido):
    campos = ['NumeroPedido', 'Nombre', 'Tamaño', 'CantidadUni', 'CantidadBultos']
    archivo_pedido = f'pedido_{fecha_pedido}_{numero_pedido}.csv'

    with open(archivo_pedido, 'w', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

        escritor_csv.writeheader()
        for producto in pedido:
            escritor_csv.writerow(producto)

    with open('pedidos.csv', 'a', newline='') as archivo_pedidos:
        escritor_csv = csv.writer(archivo_pedidos)
        escritor_csv.writerow([numero_pedido, fecha_pedido, archivo_pedido])

def realizar_devoluciones():
    clear_screen()
    print("Estás en la opción 'Realizar devoluciones que es similar a realizar pedidos'")
    submenu()




# Lógica principal

while True:
    main_menu()
    opcion = input("Ingresa el número de opción: ")

    if opcion == "1":
        realizar_pedido()
    elif opcion == "2":
        realizar_devoluciones()
    elif opcion == "3":
        calcular_volumen()
    elif opcion == "4":
        ingresar_productos()
    elif opcion == "5":
        mostrar_productos()
    elif opcion == "6":
        eliminar_producto()
    elif opcion == "7":
        mostrar_pedidos()
    elif opcion == "8":
        clear_screen()
        break
    else:
        input("Opción inválida. Presiona Enter para volver al Menú Principal.")

print("Gracias por usar el programa. ¡Hasta luego!")
