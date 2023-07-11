'''
Eliminar de una lista de números enteros los valores que se encuentren en una
segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. Ambas listas deben rellenarse con números al azar. La cantidad y el
rango de los valores los decide el programador. '''

import random
list_a=[]
list_b=[]
listR=[]
for i in range(0,19):
    list_a.append(random.randint(0,100))
for i in range(0,9):
    list_b.append(random.randint(0,100))
print('Lista original')
for num in list_a:
    print(num)
for num in list_a:
    if num in list_b:
        listR.append(num)
        list_a.remove(num)
print('Elementos a remover')
for num in listR:
    print(num)
print('Asi queda la lista')
for num in list_a:
    print(num) 
print('Lista b')
for num in list_b:
    print(num) 
  
