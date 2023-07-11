import os
os.system("clear")

class Persona:
    __nombre = str
    __edad = int
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad>= 0:
            self.__edad = nueva_edad
        else:
            print('La edad no puede ser negativa')
# Crear una instancia de la clase Persona
persona = Persona('Juan', 30)
print(persona.get_nombre())  #imprime: Juan
print(persona.get_edad())  #Imprime: 30
persona.set_edad(int(input('Ingrese la edad de Juan')))

