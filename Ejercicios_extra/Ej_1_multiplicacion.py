def multiplicacion(x,y):
    z=0
    for i in range(y):
        z+=x
    return z
pn=int(input('Ingrese el primer número: '))
sn=int(input('Ingrese el segundo número: '))
res=multiplicacion(pn,sn)
print(f'{pn} x {sn} = {res}')
