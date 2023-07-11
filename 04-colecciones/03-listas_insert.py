listmascotas=["gato","perro"]
while True:
    mascota=input("ingrese una mascota: ")
    listmascotas.insert(0,mascota)
    print(listmascotas)
    resp=input("desea ingresar otra mascota?: ")
    if resp=="no":
        break