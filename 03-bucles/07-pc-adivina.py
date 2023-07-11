numus=int(input("ingrese un número entre 0 y 100: "))
intentos=0
nupc=50
max=101
min=-1
while True:
    if numus==nupc:
        print("la pc acertó en el", intentos,"intento")
        break
    if numus>nupc:
        min=nupc
        nupc=nupc+(max-min)//2
        intentos=intentos+1
        print(nupc)
    elif numus<nupc:
        max=nupc
        nupc=nupc-(max-min)//2
        intentos=intentos+1
        print(nupc)

