

from os import listdir, getcwd
fichero = open('saludo_en_archivo.txt', 'w')
print("Hola mundo", file=fichero)
fichero.close()
for elemento in listdir(getcwd()):
    print(" *", elemento)

"""
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