import random
from statistics import median


# ----  Ejercicios ---- 

#Ejercicio 1

def muestraMenu():
    
    print("1 - Guardar asignatura")
    print("2 - Borrar asignatura")
    print("3 - Ver Nota media")
    print("4 - Ver todas las asignaturas")
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
    auxbandera = False
    while auxbandera == False:
        try:
            numAsignaturas = int(input("¿Cuántas asignaturas vas a añadir?: "))
            auxbandera = True
        except:
            print("Valor incorrecto")
    
    for i in range(0, numAsignaturas):
        materia = input("Añade la asignatura: ")
        materia = materia.upper()
        asignaturas.append(materia)
    
    return asignaturas


#Fin ejercicio 3

#Ejercicio4

def opcion2(asignaturas):
    deleteasignatura = input("Introduce el nombre de la asignatura que deseas eliminar: ")
    deleteasignatura = deleteasignatura.upper()

    for i in asignaturas:
        if asignaturas == deleteasignatura:
            asignaturas.pop(i)
            return True
    
    return False
    
#Fin ejercicio 4

#Ejercicio5

def numAleatorio():
    numAle = []
    numNotas = int(input("¿Cuántas notas vas a introducir?: "))
    num = 0

    for i in range(0, numNotas):
        num = random.randint(0, 10)
        numAle.append(num)
    
    return numAle

#Fin ejercicio 5

#Ejercicio 6

def opcion3():
    numAle = numAleatorio()
    total = 0
    contador = 0

    for i in numAle:
        total = total + i
        contador = contador + 1
    
    media = total / contador
    
    return media

#Fin ejercicio 6

#Ejercicio 7

def opcion4(asignaturas):
    print("*** Asignaturas matriculadas ***")
    contador = 0

    for i in asignaturas:
        contador = contador + 1
    
    for i in range(0, contador):
        print(i+1, "-", asignaturas[i])
    
    print("*** Fin asignaturas matriculadas ***")

#Fin ejercicio 7

# ---- Programa principal ----

asignaturas = []

#Ejercicio 2

opc = muestraMenu()

while (opc >= 1) and (opc < 5):
    if opc == 1:
        asignaturas = opcion1(asignaturas)
        print("")
    elif opc == 2:
        borrarAsignatura = opcion2(asignaturas)
        print("")
    elif opc == 3:
        notaMedia = opcion3()
        print("La media de las asignaturas es: ", notaMedia)
        print("")
    elif opc == 4:
        opcion4(asignaturas)

    opc = muestraMenu()

#Fin ejercicio 2