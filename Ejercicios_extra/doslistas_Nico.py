import random

def crear_lista_azar(cantidad, inicio, fin):
    lista = [random.randint(inicio, fin) for _ in range(cantidad)]
    return lista

def eliminar_valores(lista_original, lista_eliminar):
    lista_resultante = [num for num in lista_original if num not in lista_eliminar]
    return lista_resultante
# Generar la primera lista con números al azar
cantidad_lista_original = 10
rango_inicio_lista_original = 1
rango_fin_lista_original = 100

lista_original = crear_lista_azar(cantidad_lista_original, rango_inicio_lista_original, rango_fin_lista_original)
# Generar la segunda lista con números al azar
cantidad_lista_eliminar = 5
rango_inicio_lista_eliminar = 1
rango_fin_lista_eliminar = 50

lista_eliminar = crear_lista_azar(cantidad_lista_eliminar, rango_inicio_lista_eliminar, rango_fin_lista_eliminar)
# Imprimir las listas generadas
print("Lista original:", lista_original)
print("Lista de valores a eliminar:", lista_eliminar)
# Eliminar los valores de la segunda lista de la primera lista
lista_resultante = eliminar_valores(lista_original, lista_eliminar)

# Imprimir la lista resultante
print("Lista resultante:", lista_resultante)