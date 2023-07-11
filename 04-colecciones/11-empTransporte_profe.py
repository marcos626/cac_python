import os
def menu():
    print("Menu de opciones")
    print("\t 1. listar estaciones de ida")
    print("\t 2. listar estaciones de vuelta")
    print("\t 3. agregar estacion intermedia")
    print("\t 4. vender pasaje")
    print("\t 5. salir")
    opcion = int(input("Ingrese una opcion: "))
    os.system("clear")
    return opcion
def listarEstaciones(estaciones, tipo="ida"):
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
    print("Habilitar estacion")
    listarEstaciones(estaciones)
    id = int(input("Ingrese el id de la estacion: "))
    for estacion in estaciones:
        if estacion["id"] == id:
            estacion["estado"] = "habilitado"
            print("Estacion habilitada")
            return
    print("No se encontro la estacion")
def venderPasaje(estaciones):
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
estaciones=[
    {"id":1,"nombre":"Paso de los Libres","horaSalida":"08:00","horaLlegada":"19:00","precioIda":0,"precioVuelta":900,"estado":"habilitado"},
    {"id":2,"nombre":"Guaviraví","horaSalida":"08:45","horaLlegada":"18:15","precioIda":100,"precioVuelta":800,"estado":"Deshabilitado"},
    {"id":3,"nombre":"La Cruz","horaSalida":"09:30","horaLlegada":"17:30","precioIda":200,"precioVuelta":700,"estado":"habilitado"},
    {"id":4,"nombre":"Las Palmitas","horaSalida":"10:15","horaLlegada":"16:45","precioIda":300,"precioVuelta":600,"estado":"Deshabilitado"},
    {"id":5,"nombre":"Colonia Arrocera","horaSalida":"11:00","horaLlegada":"16:00","precioIda":400,"precioVuelta":500,"estado":"Deshabilitado"},
    {"id":6,"nombre":"Cuay Chico","horaSalida":"11:45","horaLlegada":"15:15","precioIda":500,"precioVuelta":400,"estado":"Deshabilitado"},
    {"id":7,"nombre":"Cuay Grande","horaSalida":"12:30","horaLlegada":"14:30","precioIda":600,"precioVuelta":300,"estado":"Deshabilitado"},
    {"id":8,"nombre":"Santo Tomé","horaSalida":"13:15","horaLlegada":"13:45","precioIda":700,"precioVuelta":200,"estado":"habilitado"},
    {"id":9,"nombre":"Tareirí","horaSalida":"14:00","horaLlegada":"13:00","precioIda":800,"precioVuelta":100,"estado":"Deshabilitado"},
    {"id":10,"nombre":"Virasoro","horaSalida":"14:45","horaLlegada":"12:15","precioIda":900,"precioVuelta":0,"estado":"habilitado"},
]
# Programa principal
opcion = menu()
while opcion != 5:
    if opcion == 1:
        listarEstaciones(estaciones)
    elif opcion == 2:
        listarEstaciones(estaciones, "vuelta")
    elif opcion == 3:
        habilitarEstacion(estaciones)
    elif opcion == 4:
        print("Vender pasaje")
        venderPasaje(estaciones)
    else:
        print("Opcion incorrecta")
    opcion = menu()