print("***********")
print("Ejercicio 1")
print("***********")
print("")

print ("¿Cuanto tiempo debo estudiar para un examen?")
print ("")
X = int (input("Ingrese un tiempo en SEGUNDOS: "))
print("")

print("¿Cuanto tiempo durara el examen?, en horas, minutos y segundos.")
print("Ingrese un tiempo en segundos:")
print("")
      
Examen = int(input("SEGUNDOS A CONVERTIR:  "))

Minutos = Examen // 60
Examen_S = Examen % 60

Horas = Minutos // 60
Minutos_S = Minutos % 60
    
if Examen <= X:
    print("")
    print("El tiempo de estudio para antes del examen es:")
    print(Horas, "hor", + Minutos_S, "Min", Examen_S, "Seg")
    print("Tiempo perfecto, Estudia todos los dias ese tiempo.")
elif Examen > X:
    print("")
    print("El tiempo de estudio para antes del examen es:")
    print(Horas, "hor", + Minutos_S, "Min", Examen_S, "Seg")
    print("Tiempo insuficiente, agrega mas segundos de estudio.")
else:
    print("Tiempo no encontrado")


