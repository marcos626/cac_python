def esmultiplo (x,y):
    if x%y==0:
        return True
    else:
        return False

pn=int(input('Ingrese el primer número: '))
sn=int(input('Ingrese el segundo número: '))
print(esmultiplo(pn,sn))