"""
3. Comprobación de un número Primo:
Crea un programa que verifique si un número ingresado por el usuario es primo. Un número primo es aquel que 
solo es divisible por 1 y por si mismo.
"""
import os
os.system("clear")
num=int(input('Ingrese un número: '))
for i in range(2,num):
    if num % i == 0:
        print('El número no es primo.')
        break
else: print('El número es primo')

