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
        return x
    def restaDos(self):
        x = self.__n1 - self.__n2
        return x
    def multiplicaDos(self):
        x = self.__n1 * self.__n2
        return x
    def divideDos(self):
        x = self.__n1 / self.__n2
        return x

x=int(input('Ingrese el primer número: '))
y=int(input('Ingrese el segundo número: '))
calc=calculadora(x,y)
print(f'{x} + {y} = {calc.sumaDos()}')
calc.restaDos()
print(f'{x} - {y} = {calc.restaDos()}')
calc.multiplicaDos()
print(f'{x} * {y} = {calc.multiplicaDos()}')
calc.divideDos()
print(f'{x} / {y} = {calc.divideDos() :0.2f}')
