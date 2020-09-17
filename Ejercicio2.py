print("***********")
print("Ejercicio 2")
print("***********")
print("")
print("Naturaleza de las raices")
print("Dado la ecuacion de 2do grado ax^2+bx+c=0")
print("De valores enteros para:  a,b,c")
print("")
print("")
a = int(input("Ingrese el valor para a:  "))

b = int(input("Ingrese el valor para b:  "))

c = int(input("Ingrese el valor para c:  "))

print ("\n=======================================\n")
print("Su ecuasion de segundo grado es: ", + a,"x^2+", + b,"x+", + c,"=0")
print ("\n=======================================\n")

print("¿Desea saber el discriminante de su ecuasion de 2do grado?")
print("1)Si           2)No")

inciso = int (input ("Escoja el numero:  "))

print ("\n=======================================\n")

if inciso == 1:
    D = b**2-(4*a*c)
    print("El discriminante de su ecuacion es: ", + D)
    print("Y su naturaleza de raiz son las: ")
    if D > 0:
        print(" Raices Reales y diferentes")
    elif D == 0:
        print("Raices Relaes e Iguales")
    elif D < 0:
        print("Raices complejas")
    else:
        print("Que numero habras puesto")
elif inciso == 2:
    print ("Fin")
else:
    print("Numero no encontrado")

print ("\n=======================================\n")   
