"""
docstring
Programa principal Empresa de transporte
"""
from lib_santillan import modulo_santillan as ms #ms para que quede más cortito a la hora de usarlo
""" Creo el diccionario"""
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
opcion = ms.estaciones.menu()
while opcion != 5: #Permanecemos en el while de forma indefinida, hasta que se elija la opción 5.
    if opcion == 1:
        ms.listarEstaciones(estaciones)
    elif opcion == 2:
        ms.listarEstaciones(estaciones, "vuelta")
    elif opcion == 3:
        ms.habilitarEstacion(estaciones)
    elif opcion == 4:
        print("Vender pasaje")
        ms.venderPasaje(estaciones)
    else:
        print("Opcion incorrecta")
    opcion = ms.estaciones.menu()