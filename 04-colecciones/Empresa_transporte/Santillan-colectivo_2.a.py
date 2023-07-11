import os
os.system('clear')
from colorama import Fore, init
init(autoreset=True)
recorrido=['Paso de los Libres','','La Cruz','','','','','Santo Tomé','','Gobernador Virasoro']
paradas_intermedias=['','Guaviravi','','Las Palmitas','Col. Arrocera','Cuay Chicho','Cuay Grande','','Tareiri','']
flag=False
while True:
    sel=int(input("Presione 1 para seleccionar el sentido del recorrido. 2 para agregar paradas. 9 para finalizar: "))
    if sel==1:
        sentido=int(input('ingrese el sentido del recorrido: ida: 1, regreso: 2: '))
        if sentido==1:
            os.system("clear")
            if flag==1:
                recorrido.reverse()
                flag=0
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    print(i,recorrido[i])
        elif sentido==2:
            os.system("clear")
            recorrido.reverse()
            flag=1
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    print(i,recorrido[i])
            
    
    if sel==2:
        os.system("clear")
        if flag==1:
            recorrido.reverse()
            flag=0
        for i in range(len(paradas_intermedias)): #muestro la lista de paradas intermedias
            if paradas_intermedias[i]!='':
                print(i, paradas_intermedias[i])
        nueva_parada=int(input('Presione el número de la parada que desea agregar: '))
        os.system("clear")
        if nueva_parada==1:
            recorrido[1]=paradas_intermedias[1]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[1]}. El recorrido quedó asi: ")
            paradas_intermedias[1]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[1]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])
        if nueva_parada==3:
            recorrido[3]=paradas_intermedias[3]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[3]}. El recorrido quedó asi: ")
            paradas_intermedias[3]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[3]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])
        if nueva_parada==4:
            recorrido[4]=paradas_intermedias[4]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[4]}. El recorrido quedó asi: ")
            paradas_intermedias[4]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[4]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])
        if nueva_parada==5:
            recorrido[5]=paradas_intermedias[5]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[5]}. El recorrido quedó asi: ")
            paradas_intermedias[5]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[5]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])
        if nueva_parada==6:
            recorrido[6]=paradas_intermedias[6]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[6]}. El recorrido quedó asi: ")
            paradas_intermedias[6]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[6]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])
        if nueva_parada==8:
            recorrido[8]=paradas_intermedias[8]
            print(Fore.GREEN + f"Se agregó la parada {paradas_intermedias[8]}. El recorrido quedó asi: ")
            paradas_intermedias[8]='' #vacío el contenido del elemento pero no lo elimino
            for i in range(len(recorrido)):
                if recorrido[i]!='':
                    if recorrido[i]==recorrido[8]: #para colorear el elemento nuevo
                        print(Fore.BLUE + recorrido[i])
                    else:
                        print(i,recorrido[i])   
    if sel==9:
        print('Que tenga un buen viaje')
        break
    
    
