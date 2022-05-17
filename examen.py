import random


# ----  Ejercicios ---- 

#Ejercicio 1

def muestraMenu():
    
    print("1 - Guardar asignatura")
    print("2 - Borrar asignatura")
    print("3 - Ver Nota media")
    print("4 - ver todas las asignaturas")
    print("5 - Salir")

    bandera = False

    while bandera == False:
        try:
            opc = int(input("Introduce una opcion: "))
            print("")
            bandera = True
        except:
            print("NO es una opción correcta\n")
            bandera = False

    if opc == 5:
        print("Saliendo del programa...")
    return opc

#Fin ejercicio 1

#Ejercicio 3

def opcion1(asignaturas):
    numAsignaturas = int(input("¿Cuántas asignaturas vas a añadir?: "))
    
    for i in range(0, numAsignaturas):
        materia = input("Añade la asignatura: ")
        asignaturas.append(materia)
    
    return asignaturas


#Fin ejercicio 3


# ---- Programa principal -----

asignaturas = []

#Ejercicio 2

opc = muestraMenu()

while (opc >= 1) and (opc < 5):
    if opc == 1:
        asignaturas = opcion1(asignaturas)
    elif opc == 2:
        print("2 - Borrar asignatura")
    elif opc == 3:
        print("3 - Ver Nota media")
    elif opc == 4:
        print("4 - ver todas las asignaturas")

    opc = muestraMenu()

#Fin ejercicio 2