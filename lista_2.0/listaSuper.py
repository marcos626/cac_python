#https://stackoverflow.com/questions/74828430/is-there-an-easier-way-to-filter-out-rows-from-multiple-csv-files-and-paste-them
#en esa página encontré una forma diferente de utilizar glob.glob: csvfiles = glob.glob(os.path.join(mycsvdir, '*.csv'))

import os, glob
import pandas as pd
print(os.getcwd())
listaCompras=[]
op=int()
op2=str()
mycsvdir = '/home/marcos/cac_python/lista_2.0/listas'

# pregunto si quiere abrir una lista o crear una nueva
os.system("clear")
print("1 abrir una lista")
print("2 crear una nueva")
print("3 eliminar una lista")
op = int(input("seleccione una opcion: "))
if op==1:
    os.system("clear")
    # Mostrar las listas disponibles
    csvfiles = glob.glob(os.path.join(mycsvdir, '*.csv')) # csvfiles es una lista con todos los archivos csv
    i=0
    for csvfile in csvfiles:
        print(f"{i} - {csvfile}")
        i+=1
    op = int(input("seleccione un archivo: "))
    fileSelected = csvfiles[op]

while op!=4:
    os.system("clear")
    print("******Lista de compras******")
    print("1)- Agregar articulos      *")
    print("2)- Eliminar articulos     *")
    print("3)- Imprimir Lista         *")
    print("4)- Salir del sistema      *")
    print("****************************")
    op=int(input("Seleccione una opcion: "))
    if op==1:
        os.system("clear")
        cant = input("ingrese la cantidad necesaria: ")
        articulo = input("Escriba el articulo que desea agregar a la lista: ")
        rubro = input("ingrese el rubro: ")
        # posibles rubros lacteos, limpieza, carniceria, verduleria, panificados
        #listaCompras.append(articulo)
        with open(fileSelected,'a') as milista: #https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
            milista.write(cant + "," + articulo + "," + rubro + "\n")
    elif op==2:
        df=pd.read_csv(fileSelected)
        print(df)
        #eliminar un registro del csv
        sacar=int(input('Ingrese el índice del producto que desea quitar: '))    
        df.drop(sacar, axis=0,inplace=True)
        print(df)
        df.to_csv(fileSelected, index=False)
        #os.system("clear")
    elif op==3:
        os.system("clear")
        df=pd.read_csv(fileSelected)
        print(df)
        #agrupar por rubro para mostrar ordenados
        
        op2=input("Desea agregar o quitar mas articulos?: [S/N]")
        if op2=="s":
            op=int(1)
            os.system("clear")
        elif op2=="n":
            op=4
        else:
            print("no es una opcion valida")
            op=0
print("")
print("Lista de compras terminada")
