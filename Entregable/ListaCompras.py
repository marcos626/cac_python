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
from moduloSantillan import ListaCompras
os.system('clear')
op1=int()
op2=str()
csvdir='/home/marcos/cac_python/Entregable' #defino la carpeta de trabajo
print(f'mycsvdir es: {csvdir}')
lc = ListaCompras(op1,op2,csvdir) #instancio la clase ListaCompras
op1=lc.menuSeleccionArchivos()
if op1==1: #Abrir lista existente
    fileSelected = lc.AbrirArchivo(csvdir)
elif op1==2: #Crear lista nueva
    lc.CrearArchivo(csvdir)
    input('El archivo se creó satisfactoriamente. Presione cualquier tecla para continuar')
    op1=lc.menuSeleccionArchivos()
elif op1==3: #Eliminar lista
    borrar=lc.AbrirArchivo(csvdir)
    os.remove(borrar)
    input('El archivo se borró satisfactoriamente. Presione cualquier tecla para continuar')
    op1=lc.menuSeleccionArchivos()
elif op1==4:
    print('Salir')
    
"""----------- Menu Edición de listas ----------"""

while op1!=4:
    op1=lc.menu_ABM_listas()
    if op1==1:   #Agregar artículos
        os.system('clear')
        print(f'el archivo elegido es {fileSelected}')
        df=pd.read_csv(fileSelected)
        print(df)
        cant=input('ingrese la cantidad necesaria: ')
        articulo=input('Escriba el artículo que desea agregar a la lista: ')
        rubro=input('ingrese el rubro: ')
        #posibles rubros: lacteos, limpieza, carnicería, verdulería, panificados
        with open(fileSelected,'a') as milista: #https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
            milista.write(cant + "," + articulo + "," + rubro + "\n")
              
    elif op1==2: #Eliminar artículos
        os.system("clear")
        try:
            df=pd.read_csv(fileSelected)
            print(df)
            regToBeDroped=int(input('Ingrese el índice del producto que desea quitar: '))    
            df.drop(regToBeDroped, axis=0,inplace=True)
            print(df)
            df.to_csv(fileSelected, index=False)
        except KeyError:
            print('Intenta borrar un ítem inexistente')
        input('presione cualquier tecla para volver al menu de edición de la lista')

    elif op1==3: #imprimir lista
        os.system("clear")
        df=pd.read_csv(fileSelected)
        print(df)
        #agrupar por rubro para mostrar ordenados
        
        op2=input("Desea seguir editando esta lista?: [S/N]")
        if str.lower(op2) == 's':
            op1=1 #para continuar en este menu
            os.system("clear")
        elif str.lower(op2) == "n":
            break
        else:
            print("no es una opcion valida")
            break
print("")
print("Lista de compras terminada")