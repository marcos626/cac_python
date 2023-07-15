"""

módulo contenedor de la clase Lista_compras y sus métodos para manejo de archivos csv.
"""

import os, glob
import pandas as pd
import platform
from os.path import normpath

class Multiplataforma:
    """ Clase contenedora de métodos para correr el código en distintos sistemas operativos"""
    def __init__(self):
        pass
    def clear_screen(self):
        """ Método multiplataforma para limpiar pantalla
        platform.system returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. 
        An empty string is returned if the value cannot be determined.
        """
        os.system('cls' if platform.system == 'Windows' else 'clear')
        return
    def normalizarRuta(self,ruta):
        """Método que, en función del sistema operativo
        acondiciona la dirección, por ejemplo, invierte las barras para 
        que sea compatible con Windows"""
        self.ruta=ruta
        normpath(self.ruta)
        return self.ruta

class ListaCompras:
    """ Esta clase tiene métodos para manejo de archivos """
    
    def __init__(self, op1, op2):
        self.op1=op1
        self.op2=op2
         
    def menuSeleccionArchivos(self):
        """ Muestra un menú con 4 opciones: abrir una lista, crear lista nueva, eliminar lista o salir"""
        print('Menu de selección de listas de compras')
        print("1 Abrir lista existente")
        print("2 Crear lista nueva")
        print("3 Eliminar una lista")
        print("4 Salir")
        op=int(input('Seleccione una opción: '))
        return op

    def menu_ABM_listas(self):
        """ Muestra un menú con 4 opciones y devuelve un int con  la opción elegida"""
        print("******Lista de compras******")
        print("1)- Agregar articulos      *")
        print("2)- Eliminar articulos     *")
        print("3)- Mostrar lista         *")
        print("4)- Salir                  *")
        print("****************************")
        op=int(input("Seleccione una opción: "))
        return op

    def AbrirArchivo(self):
        """ Muestra una lista con todos los archivos .csv y permite elegir alguno de ellos"""
        try:
            print('Estoy dentro de la Función AbrirArchivo')
            os.chdir(os.getcwd()+'/Entregable')
            cwd=os.getcwd()
            print(f'cwd es {cwd}')
            csvfiles=glob.glob(os.path.join(cwd, '*.csv')) #csvfiles es una lista con todos los archivos .csv encontrados
            i=0
            for csvfile in csvfiles:
                print(f'{i} - {csvfile}')
                i+=1
            op=int(input('Seleccione un archivo: '))
            fileSelected=csvfiles[op]
            os.chdir('..')    
            return fileSelected
        except IndexError:
            print('IndexError: Eligió un archivo inexistente')
        except ValueError:
            print('ValueError: Debe introducir un índice, no el nombre del archivo')
        input('Presione cualquier tecla para volver al menu de selección de archivo')
        os.chdir('..')
        ListaCompras.AbrirArchivo(self)



    def CrearArchivo(self):
        """ Crea un archivo .csv con encabezado: cantidad, producto y rubro."""
        print('Dentro de la función CrearArchivo')
        print(f'Estoy parado en la carpeta: {os.getcwd()}')
        os.chdir(os.getcwd()+'/Entregable')
        cwd=os.getcwd()
        print(f'Luego del chdir, ahora estoy en: {os.getcwd()}')
        csvfiles=glob.glob(os.path.join(cwd, '*.csv')) #csvfiles es una lista con todos los archivos .csv encontrados
        data={
            'cantidad':[],
            'producto':[],
            'rubro':[]}
        df=pd.DataFrame(data)
        nombre=input('ingrese el nombre de la nueva lista: ')
        csvfiles=glob.glob(os.path.join(cwd, '*.csv')) #lista con todos los archivos .csv
        newFile=(f'{cwd}/{nombre}.csv')
        print(f'El archivo nuevo es: {newFile}')
        for csvfile in csvfiles: #estructura de control For-else para encontrar un archivo
            if csvfile == (newFile):
                print('Ya existe un archivo con ese nombre, pruebe con otro nombre')
                os.chdir('..') #vuelvo a la carpeta original
                ListaCompras.CrearArchivo(self)
        else: #Si no encontró ninguno con el mismo nombre, continua con el else
            df.to_csv(newFile, index=False)
            os.chdir('..') #vuelvo a la carpeta original
            print(f'Vuelvo a la carpeta original {os.getcwd()}') #me fijo en que carpeta estoy
            return newFile
