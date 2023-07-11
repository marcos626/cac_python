#https://www.techiedelight.com/es/reverse-list-python/
#https://es.stackoverflow.com/questions/384666/crear-una-lista-invertida-sin-usar-metodo-reverse#:~:text=Puedes%20invertir%20la%20lista%20en%20una%20sola%20operaci%C3%B3n%20usando%20rebanado%20de%20listas.&text=La%20sintaxis%20de%20un%20rebano,a%20trav%C3%A9s%20de%20la%20lista.

import os
os.system("clear")
salida=["Paso de los Libres","La Cruz","Santo Tomé","Gobernador Virasoro"]
regreso = salida[::-1] #con slices invierto el sentido
#regreso=list(reversed(salida))
while True:
    sentido=input("ingrese el sentido del recorrido: salida o regreso: ")
    if sentido=='salida':
        print(salida)
    elif sentido=='regreso':
        print(regreso)
    elif sentido=='salir':
        print("chau")
        break