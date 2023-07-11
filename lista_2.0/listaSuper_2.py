"""
https://stackoverflow.com/questions/74828430/is-there-an-easier-way-to-filter-out-rows-from-multiple-csv-files-and-paste-them
En esa página encontré una forma diferente de utilizar glob.glob: csvfiles = glob.glob(os.path.join(mycsvdir, '*.csv'))
porque no me funcionaba de la otra manera, que vimos en clase.

Implementé la palabra reservada with para agregar nuevos registros porque no funciona bien con open. Cuando agrego el 
segundo artículo recién aparece el primero
Basado también en algunas modificaciones que introdujo Juan Ignacio Brady
"""

import os, glob
import pandas as pd
from os import remove
os.system('clear')
op1=int()
op2=int()
mycsvdir = '/home/marcos/cac_python/lista_2.0/listas'

def menu1():
    print("1 abrir una lista")
    print("2 crear una nueva")
    print("3 eliminar una lista")
    print("4 salir")
    op=int(input('Seleccione una opción: '))
    return op

def menu2():
    os.system("clear")
    print("******Lista de compras******")
    print("1)- Agregar articulos      *")
    print("2)- Eliminar articulos     *")
    print("3)- Imprimir Lista         *")
    print("4)- Salir del sistema      *")
    print("****************************")
    op=int(input("Seleccione una opcion: "))
    return op

def AbrirArchivo():
    archivos=glob.glob(os.path.join(mycsvdir, '*.csv'))
    i=0
    for archivo in archivos:
        print(f'{i} - {archivo}')
        i+=1
    op=int(input('seleccione un archivo: '))
    archElegido=archivos[op]
    return archElegido

def CrearLista():
    data={
        'cantidad':[],
        'producto':[],
        'rubro':[]}
    df=pd.DataFrame(data)
    nombre=input('ingrese el nombre de la nueva lista: ')
    archivos=glob.glob(os.path.join(mycsvdir, '*.csv'))
    for archivo in archivos:
        if archivo==(f'/home/marcos/cac_python/lista_2.0/listas\{nombre}.csv'):
            print('Este nombre de archivo ya existe, intente de nuevo')
            CrearLista()
        else:
            df.to_csv(f'/home/marcos/cac_python/lista_2.0/listas\{nombre}.csv', index=False)
            archivo=(f'/home/marcos/cac_python/lista_2.0/listas\{nombre}.csv')

while op1!=4:
    op1=menu1()
    if op1==1:
        archElegido=AbrirArchivo()
        break
    elif op1==2:
        CrearLista()
    elif op1==3:
        borrar=AbrirArchivo()
        remove(borrar)

#segunda parte del menu
while op2!=4:
    op2=menu2()
    if op2==1:
        os.system('clear')
        df=pd.read_csv(archElegido)
        print(df)
        cant=input('ingrese la cantidad necesaria: ')
        articulo=input('Escriba el artículo que desea agregar a la lista: ')
        rubro=input('ingrese el rubro: ')
        #posibles rubros: lacteos, limpieza, carnicería, verdulería, panificados
        with open(archElegido,'a') as milista: #https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
            milista.write(cant + "," + articulo + "," + rubro + "\n")
        # milista=open(archElegido,'a')
        # milista.write(cant + ','+ articulo + ',' + rubro + '\n')
        # milista.close
        
    elif op2==2:
        os.system("clear")
        df=pd.read_csv(archElegido)
        print(df)
        sacar=int(input('Ingrese el índice del producto que desea quitar: '))    
        
        df.drop(sacar, axis=0,inplace=True) #averiguar axis e inplace!! el profe los sacó y no funcionaba
        print(df)
        df.to_csv(archElegido, index=False)
    elif op2==3:
        os.system("clear")
        df=pd.read_csv(archElegido)
        print(df)
        #agrupar por rubro para mostrar ordenados
        
        op2=input("Desea agregar o quitar más articulos?: [S/N]")
        if op2=="s":
            op=int(1)
            os.system("clear")
        elif op2=="n":
            op2=4
        else:
            print("no es una opcion valida")
            op=0
print("")
print("Lista de compras terminada")