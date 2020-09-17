print ("*******************************")
print ("Ejercicio 3 (Suma de 1 segundo)")
print ("*******************************")
print ("")
print("¿Qué hora es?")

Horas = int(input("Ingrese las horas: "))
if Horas >= 24:
    print("Hora inexsistente")
elif Horas < 24:
    print ("Horas validas")
else:
    print("Tiempo no encontrado")
    
Minutos = int(input("Ingrese los minutos: "))
if Minutos >= 60:
    print("Minutos Inexistentes")
elif Minutos < 60:
    print ("Minutos validos")
else:
    print("Tiempo no encontrado")
    
Segundos = int (input("Ingrese los segundos: "))
if Segundos >= 60:
    print("Segundos Inexistentes")
elif Segundos < 60:
    print ("Segundos validos")
else:
    print("Tiempo no encontrado")

print("Son las: ", + Horas, "Hor/", + Minutos, "Min/", + Segundos, "Seg")
print("")

Segundo_1 = int(input("Sume 1 segundo al tiempo: "))

Segundos = Segundos + Segundo_1
if Segundos > 59:
    Minutos = Minutos + 1
    if Segundos > 59:
        Minutos = Minutos + 1
        Segundos = Segundos % 60
    if Minutos > 59:
        Horas = Horas + 1
        Minutos = Minutos % 60
print("Son las: ", + Horas, "Hor/", + Minutos, "Min/", + Segundos, "Seg")



