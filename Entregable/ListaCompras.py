"""

Este código permite trabajar con archivos .csv para crear, editar o abrir listas de compras.

https://stackoverflow.com/questions/74828430/is-there-an-easier-way-to-filter-out-rows-from-multiple-csv-files-and-paste-them
En esa página encontré una forma diferente de utilizar glob.glob: csvfiles = glob.glob(os.path.join(mycsvdir, '*.csv'))
porque no encontraba los archivos de la otra manera, que vimos en clase.

Implementé la palabra reservada 'with' para agregar nuevos registros porque no funcionaba bien con open. Cuando agregaba el 
segundo artículo recién aparecía el que agregué primero. 
"""
import os
import pandas as pd
from colorama import Fore, init
init(autoreset=True)
from moduloSantillan import ListaCompras
from moduloSantillan import Multiplataforma as mf
op1=int()
op2=str()
lc = ListaCompras(op1,op2) #instancio la clase ListaCompras

while op1!=4: # Bucle de selección de archivos
    try:
        mf.clear_screen()
        op1=lc.menuSeleccionArchivos()
        if op1==1: #Abrir lista existente
            fileSelected = lc.AbrirArchivo()
            break
        elif op1==2: #Crear lista nueva
            fileSelected = lc.CrearArchivo()
            input('El archivo se creó satisfactoriamente. Presione Enter para continuar')
            break
        elif op1==3: #Eliminar lista
            fileSelected=lc.AbrirArchivo()
            os.remove(fileSelected)
            input('El archivo se borró satisfactoriamente. Presione Enter para continuar')
            break
        elif op1==4:
            print('Salir')
        else: 
            input(Fore.LIGHTRED_EX + 'Eligió una opción inexistente. Presione Enter para volver al menú de selección de listas de compras' + Fore.RESET)
    except ValueError:
            input(Fore.LIGHTRED_EX + 'ValueError: Se esperaba un entero, ingresó un caracter o un float? Presione Enter para continuar' + Fore.RESET)
                
"""----------- Menu Edición de listas de compras ----------"""

while op1!=4:
    mf.clear_screen()
    op1=lc.menu_ABM_listas()
    if op1==1:   #Agregar artículos
        mf.clear_screen()
        print(Fore.GREEN + f'el archivo elegido es {fileSelected}')
        print("")
        df=pd.read_csv(fileSelected)
        print(df)
        cant=int(input('ingrese la cantidad necesaria: '))
        while cant<=0:
            print('Error: La cantidad no puede ser menor o igual a cero')
            cant=int(input('ingrese la cantidad necesaria: '))
        articulo=input('Escriba el artículo que desea agregar a la lista: ')
        rubro=input('ingrese el rubro: ')
        #posibles rubros: lacteos, limpieza, carnicería, verdulería, panificados
        with open(fileSelected,'a') as milista: #https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
            milista.write(str(cant) + "," + articulo + "," + rubro + "\n")
              
    elif op1==2: #Eliminar artículos
        mf.clear_screen()
        try:
            df=pd.read_csv(fileSelected)
            print(df)
            regToBeDroped=int(input('Ingrese el índice del producto que desea quitar: '))    
            df.drop(regToBeDroped, axis=0,inplace=True)
            print(df)
            df.to_csv(fileSelected, index=False)
        except KeyError:
            print(Fore.RED + 'Intenta borrar un ítem inexistente')
        input('presione Enter para volver al menu de edición de la lista')

    elif op1==3: #mostrar lista
        mf.clear_screen()
        df=pd.read_csv(fileSelected)
        print(Fore.LIGHTBLUE_EX + 'Lista sin ordenar' + Fore.RESET)
        print(df)
        print('')
        byRubro=df.sort_values(['rubro','articulo'])
        byRubro.head()
        print(Fore.LIGHTCYAN_EX + 'Lista ordenada por rubro y articulo' + Fore.RESET)
        print(byRubro)
        #agrupar por rubro para mostrar ordenados
        
        op2=input("Desea seguir editando esta lista?: [S/N]")
        if str.lower(op2) == 's':
            op1=1 #para continuar en este menu
            mf.clear_screen()
        elif str.lower(op2) == "n":
            break
        else:
            print("no es una opcion valida")
            break
print("")
print(Fore.LIGHTBLUE_EX + f"Lista de compras terminada")