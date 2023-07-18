
class MiClase:
    @classmethod
    def metodo_de_clase(cls):
        print("Este objeto es de la clase {}".format(cls))

instancia = MiClase()
instancia.metodo_de_clase()


"""
------------------------------------
def cero_al_diez():
    i = 0
    while i < 11:
        yield i
        i += 1

def generador():
    yield from cero_al_diez()
    yield from ("a", "e", "i", "o", "u")

for i in generador():
    print(i)

------------------------------
def generador(num):
    i = 1
    while i <= num:
        yield i
        i += 1
for i in generador(5):
    print(i)


-----------------------------------------------------
clausura: tiene el mismo efecto de usar variables globales, pero es mejor
def clausura():
    cosa = 0
    def interna():
        nonlocal cosa
        cosa += 1
        print(cosa)
    return interna

mi_funcion = clausura()
mi_funcion()
mi_funcion()
mi_funcion()
mi_funcion()
mi_funcion()

----------------------------------------------
def decorador(func):
    def interna():
        print('~~~~~~~~~~')
        func()
        print('~~~~~~~~~~')
    return interna

def mi_funcion():
    print('Hola mundo')

print('Antes de decorar:')
mi_funcion()
mi_funcion = decorador(mi_funcion)
print('Despues de decorar:')
mi_funcion()

-------------------------------------------------------
el atributo de la instancia tiene prioridad respecto del de la clase:

class C:
    x = "En la clase"
i = C()
i.x = "En la instancia"
print(C.x)
print(type(i).x)
print(i.x)

----------------------------
Muestra los datos de mi notebook:

import os
sistema = os.uname()
print("sysname:", sistema.sysname)
print("nodename:", sistema.nodename)
print("release:", sistema.release)
print("version:", sistema.version)
print("machine:", sistema.machine)
"""
