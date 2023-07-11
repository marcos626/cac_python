
class mascota:
    __anioNac=int
    nombre=str
    tipo=str
    sonido=str
    def __init__(self, nombre, tipo, sonido, nac):
        self.nombre=nombre
        self.tipo=tipo
        self.sonido=sonido
        self.__anioNac=nac
    def comunicarse(self):
        print(f'{self.nombre} está {self.sonido}')
    def get__anioNac(self):
        return self.__anioNac
    def __str__(self):
        return (f'la mascota tiene por nombre: {self.nombre}, y es un {self.tipo}')
    
mimascota=mascota('capitan','labrador','ladrando',2017)
mimascota.comunicarse()
print(mimascota)
print(f'La mascota nació en el año {mimascota.get__anioNac()}')

