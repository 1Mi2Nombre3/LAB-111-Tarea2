print ("*******************************")
print ("Ejercicio 3 (Suma de 1 segundo)")
print ("*******************************")
print ("")
print("¿Qué hora es?")

print ("\n=======================================\n")
Hora = int(input("Ingrese las horas: "))
if Hora >= 24:
    print("Hora inexsistente")
elif Hora < 24:
    print ("Horas validas")
else:
    print("Tiempo no encontrado")
    
Minuto = int(input("Ingrese los minutos: "))
if Minuto >= 60:
    print("Minutos Inexistentes")
elif Minuto < 60:
    print ("Minutos validos")
else:
    print("Tiempo no encontrado")
    
Segundo = int (input("Ingrese los segundos: "))
if Segundo >= 60:
    print("Segundos Inexistentes")
elif Segundo < 60:
    print ("Segundos validos")
else:
    print("Tiempo no encontrado")
print ("\n=======================================\n")

print("Son las: ", + Hora, "Hor/", + Minuto, "Min/", + Segundo, "Seg")
print("")

Segundo_1 = int(input("Sume X segundos a la hora dada: "))

totalSec = Hora*60*60 + Minuto*60 + Segundo
totalSec = totalSec + Segundo_1 
nuevaHora = int((totalSec/60)/60)
totalSec = totalSec - nuevaHora*60*60 
nuevoMinuto = int((totalSec/60)) 
totalSec = totalSec - nuevoMinuto*60 
nuevoSec = totalSec
print("")
print("La nueva hora son: ", + nuevaHora, "Hor/", + nuevoMinuto, "Min/", + nuevoSec, "Seg")






