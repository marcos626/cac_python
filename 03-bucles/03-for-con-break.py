cadena="hola"
letra=input("ingrese la letra a buscar ")
for c in cadena:
    if c==letra:
        print("encontrada")
        break
else:
    print("no encontrada")
