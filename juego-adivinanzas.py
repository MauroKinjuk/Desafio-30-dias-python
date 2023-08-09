#Día 6-7: Juego de Adivinanzas
#Desarrolla un juego donde el programa elige un número aleatorio y el usuario debe adivinarlo. Proporciona pistas para guiar al usuario hacia la respuesta correcta.
import random
import time
from os import system

def limpiarConsola():
    """
    Función que espera 2 segundos y luego limpia la consola.
    """
    time.sleep(0.5)
    system("cls")

def genAleatorio(nMax):
    return random.randrange(1,nMax)

def juego():
    print(f"Hola! Vamos a jugar un juego donde vas a tener que adivinar un numero")
    while True:
        try:
            nMax = int(input("Ingrese el numero maximo de generacion: "))
            nIntentos = int(input("Ingrese el numero maximo de intentos: "))
            break
        except:
            print("Debe ser un numero.")
    nAle = genAleatorio(nMax)

    contador = 0

    while contador < nIntentos:
        try:
            x = int(input("Y el numero es: "))
            if x == nAle:
                print("mmm Estas seguro/a?...")
                limpiarConsola()
                print(f"Si! Felicidades! El numero aleatorio era {nAle}")
                break
            elif x < nAle:
                limpiarConsola()
                print(f"El numero es mayor a {x}")
                contador += 1
            elif x > nAle:
                limpiarConsola()
                print(f"El numero es menor a {x}")
                contador += 1
            if nIntentos-contador == 0:
                print("No te quedan intentos :(")
                print(f"El numero era: {nAle}")
                break
            print(f"Te quedan: {nIntentos-contador} intentos")
        except:
            limpiarConsola()
            print("Debes escribir un numero.")
    
juego()