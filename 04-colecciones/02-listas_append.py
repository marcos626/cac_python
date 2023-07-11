listmascotas=[]
while True:
    mascota=input("ingrese una mascota: ")
    listmascotas.append(mascota)
    print(listmascotas)
    resp=input("desea ingresar otra mascota?: ")
    if resp=="no":
        break