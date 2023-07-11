import random
num=random.randint(0,100)
print(num)
intentos=0
while True:
    numero=int(input("ingrese un número del 1 al 100: "))
    intentos=intentos+1
    if numero==num:
        print("acertó en", intentos, "intentos") 
        break
    if numero>num:
        print("el número ingresado es mayor")
        continue
    else:
        print("el número ingresado es menor") 
        continue

