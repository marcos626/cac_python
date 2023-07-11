"""

módulo contenedor de la clase Lista_compras y sus métodos para manejo de archivos csv.
"""

import os, glob
import pandas as pd

class ListaCompras:
    """ Esta clase tiene métodos para manejo de archivos """
    #la defino fuera de los métodos porque necesito que todos lo manipulen

    def __init__(self, op1, op2,csvdir):
        self.op1=op1
        self.op2=op2
        self.csvdir=csvdir
        self.csvfiles=glob.glob(os.path.join(csvdir, '*.csv')) #csvfiles es una lista con todos los archivos .csv encontrados
    
    
    def menuSeleccionArchivos(self):
        """ Muestra un menú con 4 opciones: abrir una lista, crear lista nueva, eliminar lista o salir"""
        os.system("clear")
        print('Menu de selección de listas de compras')
        print("1 abrir lista existente")
        print("2 crear lista nueva")
        print("3 eliminar una lista")
        print("4 salir")
        op=int(input('Seleccione una opción: '))
        return op

    def menu_ABM_listas(self):
        """ Muestra un menú con 4 opciones: agregar artículos, eliminar artículos, imprimir lista o salir"""
        os.system("clear")
        print("******Lista de compras******")
        print("1)- Agregar articulos      *")
        print("2)- Eliminar articulos     *")
        print("3)- Imprimir Lista         *")
        print("4)- Salir                  *")
        print("****************************")
        op=int(input("Seleccione una opcion: "))
        return op

    
    def AbrirArchivo(self,csvdir):
        """ Muestra una lista con todos los archivos .csv y permite elegir alguno de ellos"""
        try:
            csvfiles=glob.glob(os.path.join(csvdir, '*.csv')) #csvfiles es una lista con todos los archivos .csv encontrados
            i=0
            for csvfile in csvfiles:
                print(f'{i} - {csvfile}')
                i+=1
            op=int(input('seleccione un archivo: '))
            fileSelected=csvfiles[op]
            return fileSelected
        except IndexError:
            print('Eligió un archivo inexistente')

    def CrearArchivo(self,csvdir):
        """ Crea un archivo .csv con las columnas cantidad, producto y rubro."""
        print(f'Estoy parado en la carpeta: {os.getcwd()}') #me fijo en que carpeta estoy
        data={
            'cantidad':[],
            'producto':[],
            'rubro':[]}
        df=pd.DataFrame(data)
        nombre=input('ingrese el nombre de la nueva lista: ')
        csvfiles=glob.glob(os.path.join(csvdir, '*.csv')) #lista con todos los archivos .csv
        archivo_nuevo=(f'/home/marcos/cac_python/Entregable/{nombre}.csv')
        print(f'El archivo nuevo es: {archivo_nuevo}')
        for csvfile in csvfiles: #estructura de control For-else para encontrar un archivo
            if csvfile == (archivo_nuevo):
                print('Este nombre de archivo ya existe, intente de nuevo')
                ListaCompras.CrearArchivo(self,csvdir)
        else: #Si ninguno se llamaba igual, continua con el else
            ruta = os.path.join('/home/marcos/cac_python/Entregable')
            ruta2 = os.path.join('/home/marcos/cac_python')
            print(f'la ruta es {ruta}')
            os.chdir(ruta)
            print(f'Hice un chdir. Estoy parado en la carpeta {os.getcwd()}') #me fijo en que carpeta estoy
            df.to_csv(archivo_nuevo, index=False)
        #csvfile=(f'/home/marcos/cac_python/{nombre}.csv')
        os.chdir(ruta2) #vuelvo a la carpeta original
        print(f'Hice un chdir. Estoy parado en la carpeta {os.getcwd()}') #me fijo en que carpeta estoy
