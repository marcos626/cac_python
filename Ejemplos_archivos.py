op1=int(input('Íngrese un número'))
print(op1)

"""
import platform
import os
def clear_screen():
    os.system('cls' if platform.system == 'Windows' else 'clear')

clear_screen()
print(platform.system())
print(os.name)


#cambiar de archivo con os.chdir y os.getcwd
import os
print(f'la ruta actual es {os.getcwd()}')
archivo_csv='/Nico/productos.csv'
os.chdir(os.getcwd()+'/Nico')
print(f'La ruta nueva es {os.getcwd()}')
#archivo_csv=getcwd()+archivo_csv
#print(f'El archivo es {archivo_csv}')

---------------------------------------

from os import listdir, getcwd
fichero = open('saludo_en_archivo.txt', 'w')
print("Hola mundo", file=fichero)
fichero.close()
for elemento in listdir(getcwd()):
    print(" *", elemento)

----------------------------------

from os.path import normpath
paths = [
"/uno/dos/tres/./cuatro",
"/uno/dos/tres//cuatro/",
"/uno//dos/tres/otro/../cuatro/",
"/uno/dos/tres/cuatro/otro/..",
]
for path in paths:
    print(normpath(path))

----------------------------------


import csv
with open('pruebas.csv', newline="") as fichero:
    reader = csv.reader(fichero)
    for fila in reader:
        print(fila[0], fila[2])


"""