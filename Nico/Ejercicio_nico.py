from modulo import clear_screen,main_menu,realizar_pedido,realizar_devoluciones,calcular_volumen,calcular_volumen_pedido
from modulo import ingresar_productos, mostrar_contenido_archivo, mostrar_pedidos, mostrar_productos, eliminar_producto

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