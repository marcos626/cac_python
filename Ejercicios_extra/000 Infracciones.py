""" se realizó una inspección en una fábrica de pinturas y se detectaron 10 infracciones. 
De cada infracción se tomó nota de los siguientes datos:
-Tipo de infracción (1, 2, 3 o 4)
-Valor de la multa.
-Gravedad de la infracción ('L', 'M', 'G')
Usted debe realizar un programa que solicite los datos de 10 infracciones al usuario e informe, 
al final del proceso lo siguiente:
a) los valores totales de la multa a pagar de acuerdo al tipo de gravedad.
b) La leyenda "Clausurar fábrica" si la cantidad de infracciones 3 y 4 con gravedad "G" 
sean mayor a 3. """

import os
os.system("clear")

infraccion_t=[]
infraccion_g=[]
lista_infracciones=[infraccion_t,infraccion_g]
i=1
while i<=4:
    tipo=int(input(f"ingrese el tipo de infracción (1, 2, 3 o 4) de la {i}° infracción: "))
    infraccion_t.append(tipo)
    gravedad=input(f"ingrese la gravedad de la infracción ('L', 'M', 'G') de la {i}° infracción: ")
    infraccion_g.append(gravedad)
    i+=1
    #print(lista_infracciones)

count=0
multa=0
for j in range(len(infraccion_t)):
    print(infraccion_t[j])
    print(infraccion_g[j])
    print(infraccion_t[j]==3 or infraccion_t[j]==4)
    print(infraccion_g[j]=='G')
    if infraccion_t=='1':
        multa+=1000
    
    if (infraccion_t[j]==3 or infraccion_t[j]==4) and infraccion_g[j]=='G':
        count+=1
if count>1:
     print("Clausurar fábrica")