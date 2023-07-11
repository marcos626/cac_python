def sumaDos(n1,n2):
    x=n1+n2
    print(f'La suma de {n1} y {n2} es {x}')
def restaDos(n1,n2):
    x=n1-n2
    print(f'La resta de {n1} y {n2} es {x}')
def multiplicaDos(n1,n2):
    x=n1*n2
    print(f'El producto de {n1} y {n2} es {x}')    
def divideDos(n1,n2):
    x=n1/n2
    print(f'La división de {n1} y {n2} es {x}')

x=int(input('Ingrese el primer número: '))
y=int(input('Ingrese el segundo número: '))
sumaDos(x,y)
restaDos(x,y)
multiplicaDos(x,y)
divideDos(x,y)

