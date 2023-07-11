"""
3. Comprobación de un número Primo:
Crea un programa que verifique si un número ingresado por el usuario es primo. Un número primo es aquel que 
solo es divisible por 1 y por si mismo.
"""
import os
os.system("clear")
def es_primo(num):
    for n in range(2,num):
        if num % n == 0:
            print(f'No es primo, {n} es divisor')
            return
    print('Es primo')
    return
numero=int(input('Ingrese un número: '))
es_primo(numero)

