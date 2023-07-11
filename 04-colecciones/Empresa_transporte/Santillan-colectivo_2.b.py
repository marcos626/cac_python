#En este ejercicio comparo los strings de las paradas intermedias.
#uso insert y remove. Va cambiando el tamaño de ambas listas

import os
os.system('clear')
from colorama import Fore, init
init(autoreset=True)
recorrido=['Paso de los Libres','La Cruz','Santo Tomé','Gobernador Virasoro']
paradas_intermedias=['Guaviraví','Las Palmitas','Col. Arrocera','Cuay Chico','Cuay Grande','Tareirí']
flag=False
while True:
    sel=int(input("Presione 1 para seleccionar el sentido del recorrido. 2 para agregar paradas. 9 para finalizar: "))
    os.system("clear")
    if sel==1:
        sentido=int(input('Ingrese el sentido del recorrido: ida: 1, regreso: 2: '))
        os.system("clear")
        if sentido==1:
            if flag==1:
                recorrido.reverse()
                flag=0
            for i in range(len(recorrido)):
                print(i,recorrido[i])
        elif sentido==2:
            recorrido.reverse()
            flag=1
            for i in range(len(recorrido)):
                print(i,recorrido[i])
    if sel==2:
        os.system("clear")
        if flag==1:
            recorrido.reverse()
            flag=0
        for i in paradas_intermedias: #muestro la lista de paradas intermedias
            print(i)
        nueva_parada=input('Escriba la parada que desea agregar: ')
        os.system("clear")
        if nueva_parada=='Guaviraví':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='Paso de los Libres':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
        if nueva_parada=='Las Palmitas':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='La Cruz':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
        if nueva_parada=='Col. Arrocera':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='La Cruz' and recorrido[i+1]=='Las Palmitas':
                    recorrido.insert(i+2,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
        if nueva_parada=='Cuay Chico':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='La Cruz'and recorrido[i+1]=='Las Palmitas' and recorrido[i+2]=='Col. Arrocera':
                    recorrido.insert(i+3,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz'and recorrido[i+1]=='Las Palmitas':
                    recorrido.insert(i+2,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
        if nueva_parada=='Cuay Grande':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='La Cruz' and recorrido[i+1]=='Las Palmitas' and recorrido[i+2]=='Col. Arrocera' and recorrido[i+3]=='Cuay Chico':
                    recorrido.insert(i+4,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz' and recorrido[i+1]=='Las Palmitas' and recorrido[i+2]=='Col. Arrocera':
                    recorrido.insert(i+3,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz' and recorrido[i+1]=='Las Palmitas':
                    recorrido.insert(i+2,nueva_parada)
                    break
                elif recorrido[i]=='La Cruz':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
        if nueva_parada=='Tareirí':
            for i in range(len(recorrido)): #Busco el elemento anterior y luego inserto el elemento nuevo
                if recorrido[i]=='Santo Tomé':
                    recorrido.insert(i+1,nueva_parada)
                    break
            print(Fore.GREEN + f"Se agregó la parada {nueva_parada}. El recorrido quedó asi: ")
            for i in recorrido:
                if i==nueva_parada: #para colorear el elemento nuevo
                    print(Fore.BLUE + i)
                else:
                    print(i)
            paradas_intermedias.remove(nueva_parada)
    if sel==9:
        print('Que tenga un buen viaje')
        break
    
    
