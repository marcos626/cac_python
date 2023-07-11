"""" 
2. Convertidor de unidades: 
Escribe un programa que convierta una cantidad en metros a centímetros, pulgadas y pies.
Solicita al usuario la cantidad en metros y muestra los resultados convertidos.
de metros a centímetros:
mivar * 100
de metros a pulgadas:
mivar * 39.37
de metros a pies:
mivar * 3.281
"""
import os
os.system("clear")
class Converter:
    __longitud=float
    def __init__(self, longitud):
        self.__longitud=longitud
    def metros_a_centimetros(self):
        x=self.__longitud*100
        print(f'{self.__longitud} metros equivalen a {x:0.2f} centímetros')
    def metros_a_pulgadas(self):
        x=self.__longitud*39.37
        print(f'{self.__longitud} metros equivalen a {x:0.2f} pulgadas')
    def metros_a_pies(self):
        x=self.__longitud*3.281
        print(f'{self.__longitud} metros equivalen a {x:0.2f} pies')

long_metros=float(input('Ingrese la cantidad de metros que desea convertir de unidad: '))
convertidor = Converter(long_metros)
convertidor.metros_a_centimetros()
convertidor.metros_a_pulgadas()
convertidor.metros_a_pies()
