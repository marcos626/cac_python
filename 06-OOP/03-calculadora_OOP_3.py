"""
1. Calculadora de operaciones básicas:
Crea un programa que solicite al usuario dos números y realice las operaciones básicas (suma, resta, multiplicación 
y división) con ellos. Imprime los resultados.
"""
import os
os.system("clear")

class calculadora:
    def __init__(self, n1, n2):
        self.sumaDos = n1 + n2
        print(f'{n1} + {n2} = {self.sumaDos}')
        self.restaDos = n1 - n2
        print(f'{n1} - {n2} = {self.restaDos}')
        self.multiplicaDos = n1 * n2
        print(f'{n1} x {n2} = {self.multiplicaDos}')
        self.divideDos = n1 / n2
        print(f'{n1} / {n2} = {self.divideDos :0.2f}')


x=int(input('Ingrese el primer número: '))
y=int(input('Ingrese el segundo número: '))
calc=calculadora(x,y)
calc.sumaDos
calc.restaDos
calc.multiplicaDos
calc.divideDos
