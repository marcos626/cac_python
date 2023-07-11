"""
1. Calculadora de operaciones básicas:
Crea un programa que solicite al usuario dos números y realice las operaciones básicas (suma, resta, multiplicación 
y división) con ellos. Imprime los resultados.
"""
import os
os.system("clear")

class calculadora:
    __n1=float
    __n2=float
    def __init__(self, n1, n2):
        self.__n1=n1
        self.__n2=n2
    def sumaDos(self):
        x = self.__n1 + self.__n2
        print(f'{self.__n1} + {self.__n2} = {x:0.2f}')
    def restaDos(self):
        x = self.__n1 - self.__n2
        print(f'{self.__n1} - {self.__n2} = {x:0.2f}')
    def multiplicaDos(self):
        x = self.__n1 * self.__n2
        print(f'{self.__n1} x {self.__n2} = {x:0.2f}')
    def divideDos(self):
        x = self.__n1 / self.__n2
        print(f'{self.__n1} / {self.__n2} = {x:0.2f}')

#creo un diccionario llamado operaciones:
operaciones={
    1:'Suma',
    2:'Resta',
    3:'Multiplicación',
    4:'División',
}

x=float(input('Ingrese un número: '))
y=float(input('Ingrese otro número: '))
calc=calculadora(x,y) #creo el objeto calc (instancio la clase calculadora)
while True:
    print('Ingrese el número de la operación que desea realizar')
    for clave, valor in operaciones.items(): #recorro el for para mostrar la lista en pantalla
        print(clave, valor)
    op=int(input())
    if op==1:
        calc.sumaDos()
    if op==2:
        calc.restaDos()
    if op==3:
        calc.multiplicaDos()
    if op==4:
        calc.divideDos()
    continuar=input('Desea realizar otra operación? s/n\n')
    if continuar == 's':
        continue
    elif continuar == 'n':
        print('Chau')
        break