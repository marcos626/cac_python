try:
    pn=input('Ingrese un número: ')
    sn=input('Ingrese otro número: ')
    pn=int(pn)
    sn=int(sn)

    res=pn/sn
except ZeroDivisionError:
    print('No se puede dividir por cero')
except TypeError:
    print('Error de tipo de dato. No se puede dividir strings')
except ValueError:
    print('Error, el tipo de dato es int pero ud. ingresó caracteres. Ingresó un número float?')
else:
    print(f'La división da {res:.3}')

"""" tambien se puede usar:
except:
sin ningun otro tipo de error
Es un except generico
"""

