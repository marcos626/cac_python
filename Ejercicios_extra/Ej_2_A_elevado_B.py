def A_elevado_B(x,y):
    z=1
    for i in range(y):
        z*=x
    return z
pn=int(input('Ingrese el primer número: '))
sn=int(input('Ingrese el segundo número: '))
res=A_elevado_B(pn,sn)
print(f'{pn} elevado a la {sn} = {res}')