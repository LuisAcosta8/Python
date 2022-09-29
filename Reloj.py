#   Hora minutos segundos

#Bibliotecas
import time


#Declaracion de variables


hora = 0
minutos = 0
segundos = 0
titulo = "Reloj"
invalid = "Formato de hora no valido"

#Programa

print(titulo.center(70, "*"))
hora = int(input("Ingresa la hora en formato 24 hrs: "))
minutos = int(input("Ingresa los minutos: "))
segundos = int(input("Ingresa los segundos: "))
if hora >= 24 or minutos >= 60 or segundos >= 60:
    print(invalid)


#Ciclo Segundos

    
while segundos < 60:
    segundos = segundos + 1
    if segundos == 60:
        minutos = minutos + 1
        segundos = 0
    time.sleep(1)
    if minutos == 60:
        hora = hora + 1
        minutos = 0
    if hora == 24:
        hora = 0
    if hora in range(12, 24):
        print(str(hora) + " pm " + str(minutos) + " min " + str(segundos) + " seg ")
    elif hora in range(0, 12):
        print(str(hora) + " am " + str(minutos) + " min " + str(segundos) + " seg ")
