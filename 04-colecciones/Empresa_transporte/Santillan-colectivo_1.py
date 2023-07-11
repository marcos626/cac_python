import os
os.system("clear")
recorrido=["Paso de los Libres","La Cruz","Santo Tomé","Gobernador Virasoro"]
flag=False
while True:
    sentido=int(input("ingrese el sentido del recorrido: Ida = 1, regreso = 2, salir = 9: "))
    if sentido==1:
        os.system("clear")
        if flag==1:
            recorrido.reverse()
            flag=0
        for i in recorrido:
            print(i)
    elif sentido==2:
        os.system("clear")
        recorrido.reverse()
        flag=1
        for i in recorrido:
            print(i)
    elif sentido==9:
        break
