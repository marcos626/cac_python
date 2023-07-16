"""

módulo contenedor de la clase Lista_compras y Multiplataforma.
"""

import os, glob
import pandas as pd
import platform
from os.path import normpath
from colorama import Fore, init
init(autoreset=True)

class Multiplataforma:
    """ Clase contenedora de métodos para correr el código en distintos sistemas operativos"""
    def clear_screen():
        """ Método multiplataforma para limpiar pantalla
        platform.system returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. 
        An empty string is returned if the value cannot be determined.
        """
        os.system('cls' if platform.system == 'Windows' else 'clear')
        return
    
    def normalizarRuta(ruta):
        """Método que, en función del sistema operativo
        acondiciona la dirección, por ejemplo, invierte las barras para 
        que sea compatible con Windows"""
        normpath(ruta)
        return ruta

class ListaCompras:
    """ Esta clase tiene métodos para manejo de archivos .csv"""
    
    def __init__(self, op1, op2):
        self.op1=op1
        self.op2=op2
         
    def menuSeleccionArchivos(self):
        """ Muestra un menú con 4 opciones: abrir una lista, crear lista nueva, eliminar lista o salir"""
        print(Fore.LIGHTBLUE_EX + f'Menu de selección de listas de compras')
        print(Fore.LIGHTBLUE_EX + f'--------------------------------------' + Fore.RESET)
        print("1 Abrir lista existente")
        print("2 Crear lista nueva")
        print("3 Eliminar lista")
        print("4 Salir")
        print("")
        op=int(input('Seleccione una opción: '))
        return op

    def menu_ABM_listas(self):
        """ Muestra un menú con 4 opciones y devuelve un int con  la opción elegida"""
        try:
            print(Fore.LIGHTMAGENTA_EX + f"******Lista de compras******")
            print("")
            print("1)- Agregar articulos      *")
            print("2)- Eliminar articulos     *")
            print("3)- Mostrar lista          *")
            print("4)- Salir                  *")
            print("")
            op=int(input("Seleccione una opción: "))
            return op
        except IndexError:
            input(Fore.LIGHTRED_EX + 'IndexError: Eligió un archivo inexistente. Presione Enter para continuar' + Fore.RESET) 
        except ValueError:
            input(Fore.LIGHTRED_EX + 'ValueError: Debe introducir un índice, no el nombre del archivo. Presione Enter para continuar' + Fore.RESET)
        
    def AbrirArchivo(self):
        """ Muestra una lista con todos los archivos .csv y permite elegir alguno de ellos"""
        try:
            Multiplataforma.clear_screen()
            print(Fore.LIGHTBLUE_EX + 'Listas de compras disponibles' + Fore.RESET)
            print('')
            ruta = os.getcwd()+'/Entregable'
            Multiplataforma.normalizarRuta(ruta)
            os.chdir(ruta)
            cwd=os.getcwd()
            csvfiles=glob.glob(os.path.join(cwd, '*.csv')) #csvfiles es una lista con todos los archivos .csv encontrados
            i=0
            for csvfile in csvfiles:
                print(f'{i} - {csvfile}')
                i+=1
            print('')
            op=int(input('Seleccione un archivo: '))
            fileSelected=csvfiles[op]
            os.chdir('..')    
            return fileSelected
        except IndexError:
            input(Fore.LIGHTRED_EX + 'IndexError: Eligió un archivo inexistente. Presione Enter para volver al menu de selección de archivos' + Fore.RESET)
        except ValueError:
            input(Fore.LIGHTRED_EX + 'ValueError: Se esperaba un tipo de dato entero. Presione Enter para volver al menu de selección de archivos' + Fore.RESET)
        os.chdir('..') #Vuelvo a la carpeta original
        ListaCompras.AbrirArchivo(self)

    def CrearArchivo(self):
        """ Crea un archivo .csv con encabezado: cantidad, producto y rubro."""
        Multiplataforma.clear_screen()
        flag=bool()
        print('Dentro de la función CrearArchivo')
        print(f'Estoy parado en la carpeta: {os.getcwd()}')
        ruta = os.getcwd()+'/Entregable'
        Multiplataforma.normalizarRuta(ruta)
        os.chdir(ruta)
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
        Multiplataforma.normalizarRuta(newFile) #invertir las barras si está en Windows
        print(f'El archivo nuevo es: {newFile}')
        for csvfile in csvfiles: #estructura de control For-else para encontrar un archivo
            if csvfile == (newFile):
                input(Fore.LIGHTRED_EX + 'Ya existe un archivo con ese nombre, pruebe con otro nombre. Presione Enter para continuar' + Fore.RESET)
                os.chdir('..') #vuelvo a la carpeta original
                newFile = ListaCompras.CrearArchivo(self)
                if flag==True:
                    flag=False
                    break
        else: #Si no encontró ninguno con el mismo nombre, continua con el else
            df.to_csv(newFile, index=False)
            print(df)
            os.chdir('..') #vuelvo a la carpeta original
            #print(f'Vuelvo a la carpeta original {os.getcwd()}') #me fijo en que carpeta estoy
            flag=True #bandera en uno para indicar que se creó un nuevo archivo
            return newFile
