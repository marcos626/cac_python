

class MiClase:

    @staticmethod
    def metodo_estatico(x):
        print(x)

    def metodo_convencional(self, x):
        print(x)

    @classmethod
    def metodo_de_clase(cls, x):
        print(x)

instancia = MiClase()

print("En la clase:")
print("metodo_convencional es {}".format(type(MiClase.metodo_convencional)))
print("metodo_estatico es {}".format(type(MiClase.metodo_estatico)))
print("metodo_de_clase es {}".format(type(MiClase.metodo_de_clase)))

print("En la instancia:")
print("metodo_convencional es {}".format(type(instancia.metodo_convencional)))
print("metodo_estatico es {}".format(type(instancia.metodo_estatico)))
print("metodo_de_clase es {}".format(type(instancia.metodo_de_clase)))


"""
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def datos(self):
        return self.nombre + " " + self.apellido
persona = Persona("Pablo", "Hinojosa")
nombre = persona.datos()
print(nombre)

-------------------------
class Clase:
    def __init__(self):
        self.x = "Valor del atributo"
        print("iniciando una instancia")
    def muestra(self):
        print(self.x)
print("Instanciamos la clase:")
a = Clase()
print("Mostramos el atributo x:")
a.muestra()

---------------------------
class MiClase:
    @classmethod
    def metodo_de_clase(cls):
        print("Este objeto es de la clase {}".format(cls))
instancia = MiClase()
instancia.metodo_de_clase()

------------------------------------------------------
def generador():
    yield from range(3)
    yield from "AEIOU"
    yield from [i ** 3 for i in range(5)]
for i in generador():
    print(i)

-----------------------------------------------
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

"""