'''Escribir una función que reciba como parámetros un número de día, un número
de mes y un número de año y devuelva la cantidad de días que faltan hasta fin
de mes. 

Luego desarrollar tres programas para:
∑ Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días que faltan hasta fin de año.
∑ Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días transcurridos en ese año hasta esa fecha.
∑
Los tres programas deben realizar su trabajo a través de la función indicada al
comienzo'''

dia=0
mes=0
año=0
diasPorMes = { 
  1:31,
  2:28,
  3:31,
  4:30,
  5:31,
  6:30,
  7:31,
  8:31,
  9:30,
  10:31,
  11:30,
  12:31,
}
def IngresarFechaLocal():
  dia=int(input("Ingrese el dia: "))
  mes=int(input("Ingrese el mes: "))
  año=int(input("Ingrese el año: "))
  return dia,mes,año

def IngresarFecha():
  global dia,mes,año
  dia=int(input("Ingrese el dia: "))
  mes=int(input("Ingrese el mes: "))
  año=int(input("Ingrese el año: "))

def DiasFaltantesFinDeMes():
  global dia,mes,año, diasPorMes
  diasRestantes = diasPorMes[mes] - dia
  print(f'{diasPorMes[mes]} - {dia} = {diasRestantes}')
  return diasRestantes

def DiasFaltantesFinDeAño():
  global dia,mes,año,diasPorMes
  diasRestantes=mesF
  for i in range(mes+1,len(diasPorMes)):
    print(f'{diasRestantes} + {diasPorMes[i]}')
    diasRestantes+=diasPorMes[i]
  return diasRestantes

def diasTranscurridos():
  global dia,mes,año,diasPorMes 
  diasTRANS=0
  for i in range(0,mes-1):
    diasTRANS += diasPorMes[i]
  return diasTRANS

def diferencia():
  print("ingrese la primer fecha")
  fecha1=IngresarFechaLocal()
  dia1,mes1,año1=fecha1
  print("ingrese la segunda fecha")
  fecha2=IngresarFechaLocal()
  dia2,mes2,año2=fecha2  
  diferenciaDias=dia1-dia2
  diferenciaMes=mes1-mes2
  diferenciaAños=año1-año2
  return diferenciaDias,diferenciaMes,diferenciaAños

IngresarFecha()

mesF=DiasFaltantesFinDeMes()
añoF=DiasFaltantesFinDeAño()
diaT=diasTranscurridos()
print(f"Los dias restantes del mes son {mesF}")
print(f"Los dias hasta fin de año son {añoF}")
print(f"Los dias transcurridos son {diaT}")

dia3,mes3,año3=diferencia()
print(f"La diferencia entre fechas es de {dia3} dias {mes3} meses {año3} años")