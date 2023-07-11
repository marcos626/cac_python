#
palabra = str()
texto=input("ingrese su nombre: ")
for c in texto:
    if palabra == "": #si palabra está vacía que comience con la primera letra
        palabra=palabra + c
    else:
        palabra = palabra + "-" + c #con las demás letras que agregue un guión medio entre letras
print(palabra)