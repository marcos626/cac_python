"""
1. Calculadora de operaciones básicas:
Crea un programa que solicite al usuario dos números y realice las operaciones básicas (suma, resta, multiplicación 
y división) con ellos. Imprime los resultados.
"""
import os
os.system("clear")

class calculadora:
    __n1=int
    __n2=int
    
    def __init__(self, n1, n2):
        self.__n1=n1
        self.__n2=n2
    
    def sumaDos(self):
        x = self.__n1 + self.__n2
        print(f'{self.__n1} + {self.__n2} = {x}')
    
    def restaDos(self):
        x = self.__n1 - self.__n2
        print(f'{self.__n1} - {self.__n2} = {x}')
    
    def multiplicaDos(self):
        x = self.__n1 * self.__n2
        print(f'{self.__n1} x {self.__n2} = {x}')
    
    def divideDos(self):
        x = self.__n1 / self.__n2
        print(f'{self.__n1} / {self.__n2} = {x:0.2f}')

x=int(input('Ingrese el primer número: '))
y=int(input('Ingrese el segundo número: '))
calc=calculadora(x,y)
calc.sumaDos()
calc.restaDos()
calc.multiplicaDos()
calc.divideDos()
