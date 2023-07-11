"""

Provee cuatro funciones:
menu
listarEstaciones
habilitarEstacion
venderPasaje
"""

import os

class estaciones:

    def menu():
        """ docstring de función menu"""
        print("Menu de opciones")
        print("\t 1. listar estaciones de ida")
        print("\t 2. listar estaciones de vuelta")
        print("\t 3. agregar estacion intermedia")
        print("\t 4. vender pasaje")
        print("\t 5. salir")
        opcion = int(input("Ingrese una opcion: "))
        os.system("clear")
        return opcion

def listarEstaciones(estaciones, tipo="ida", estado="habilitado"):
    """ docstring de función listarEstaciones"""
    print("Listado de estaciones de " + tipo)
    if tipo == "ida":
        for estacion in estaciones:
            if estacion["estado"] == "habilitado":
                print("\tid: " + str(estacion["id"]) + " - " + estacion["nombre"] + " - " + estacion["horaSalida"] + " - " + str(estacion["precioIda"]))
    elif tipo == "vuelta":
        estaciones.reverse()
        for estacion in estaciones:
            if estacion["estado"] == "habilitado":
                print("\tid: " + str(estacion["id"]) + " - " + estacion["nombre"] + " - " + estacion["horaLlegada"] + " - " + str(estacion["precioVuelta"]))
        estaciones.reverse()
    else:
        print("Tipo de estacion incorrecta")

def habilitarEstacion(estaciones):
    """ docstring de función habilitarEstacion"""
    print("Habilitar estacion")
    listarEstaciones(estaciones,estado="deshabilitado")
    id = int(input("Ingrese el id de la estacion: "))
    for estacion in estaciones:
        if estacion["id"] == id:
            estacion["estado"] = "habilitado"
            print("Estacion habilitada")
            return
    print("No se encontro la estacion")

def venderPasaje(estaciones):
    """ docstring de función venderPasaje"""
    print("Vender pasaje")
    listarEstaciones(estaciones)
    estacionSalida=int(input("Ingrese el id de la estacion de salida: "))
    id = int(input("Ingrese el id de la estacion llegada: "))
    for estacion in estaciones:
        if estacion["id"] == id:
            if estacion["estado"] == "habilitado":
                print("\tid: " + str(estacion["id"]) + " - " + estacion["nombre"] + " - Ida " + estacion["horaSalida"] )
                print("\tid: " + str(estacion["id"]) + " - " + estacion["nombre"] + " - Regreso " + estacion["horaLlegada"] )
                tipo = input("Ingrese el tipo de pasaje (ida/vuelta): ")
                if tipo == "ida":
                    print("\tEl precio del pasaje es: " + str(estacion["precioIda"] - estaciones[estacionSalida-1]["precioIda"] ))
                elif tipo == "vuelta":
                    print("\tEl precio del pasaje es: " + str( estacion["precioVuelta"] - estaciones[estacionSalida-1]["precioVuelta"] ))
                else:
                    print("Tipo de pasaje incorrecto")
            else:
                resp=input("La estacion no esta habilitada la desea habilitar? (s/n): ")
                if resp=="s":
                    estacion["estado"] = "habilitado"
                    print("Estacion habilitada nuevamente para la venta de pasajes")
                    venderPasaje(estaciones)
            return
    print("No se encontro la estacion")
