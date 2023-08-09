#Día 6-7: Juego de Adivinanzas
#Desarrolla un juego donde el programa elige un número aleatorio y el usuario debe adivinarlo. Proporciona pistas para guiar al usuario hacia la respuesta correcta.
import random

def genNumeroAleatorio():
    while True:
        try:
            x = int(input("Ingrese numero maximo a adivinar: "))
            break
        except:
            print("Debes elegir un numero entero.")
        finally:
            nRandom = random.randint(1,x)
    return nRandom

def ayudas(elec,nrandom):
    if elec > nrandom:
        print(f"El numero es menor a {elec}")
    if elec < nrandom:
        print(f"El numero es mayor a {elec}")
    return True

def adivinanza():
    x = genNumeroAleatorio()
    intentosMax = input("Cuantos intentos maximos deseas tener?")
    print(x)
    print(f"Debes adivinar el numero que se encuentra entre 1 y {x}")

    contador = 0
    while contador <= intentosMax:
        elec1 = int(input("Escribe el numero:"))
        if elec1 > x:


    if elec1 != x:
        ayudas(elec1,x)


adivinanza()