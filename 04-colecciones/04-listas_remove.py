import os
os.system("clear")
listMascotas=[]
while True:
    print("1 para agregar mascotas")
    print("2 para eliminar mascotas de la lista")
    print("3 para modificar mascotas")
    print("4 para listar")
    print("5 para salir")
    op=int(input("ingrese una opción: "))
    if op==1:
        mascota=input("ingrese una mascota: ")
        listMascotas.insert(0,mascota)
        print(listMascotas)
    elif op==2:
        resp=input("que elemento quiere eliminar?: ")
        listMascotas.remove(resp)
        print(listMascotas)
    elif op==3:
        resp=input("ingrese la mascota a modificar: ")
        nuevoelemento=input("ingrese el nuevo valor: ")
        listMascotas[listMascotas.index(resp)]=nuevoelemento
        print(listMascotas)
    elif op==5:
        break
    



    