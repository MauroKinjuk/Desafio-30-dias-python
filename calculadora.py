#Primer proyecto de los 30 Dias
#Una calculadora básica
import msvcrt

def suma(a,b):
    return (a + b)

def multiplicacion(a,b):
    return (a * b)

def division(a,b):
    return (a / b)

def resta(a,b):
    return (a - b)

def principal():
    print(f"\nHola! Esta es una calculadora super básica realizada en python.")
    print("La misma contiene: suma, multiplicación, division y resta")

def inicializacion():
    print(f"\nPresiona la tecla veas a continuacion para seleccionar la operacion que deseas realizar: ")
    print("[S]: Suma")
    print("[R]: Resta")
    print("[D]: Division")
    print("[M]: Multiplicacion")
    print("[E]: Salir")

    while True:
        opcion = msvcrt.getwch()

        if opcion == 's' or opcion == 'S':
            print("Que numeros deseas sumar?")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print(f"La suma de {a} y {b} es: ", suma(a,b))
            inicializacion()
        if opcion == 'r' or opcion == 'R':
            print("Que numeros deseas restar?")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print(f"La resta de {a} y {b} es: ", resta(a,b))
            inicializacion()
        if opcion == 'd' or opcion == 'D':
            print("Que numeros deseas dividir?")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print(f"La division de {a} y {b} es: ", division(a,b))
            inicializacion()
        if opcion == 'm' or opcion == 'M':
            print("Que numeros deseas multiplicar?")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print(f"La multiplicacion de {a} y {b} es: ", multiplicacion(a,b))
            inicializacion()
        if opcion == 'e' or opcion == 'E':
            exit()

    
principal()
inicializacion()