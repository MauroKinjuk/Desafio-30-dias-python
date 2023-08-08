#Día 5: Convertidor de Unidades
#Escribe un programa que convierta unidades de longitud, como metros a pies, o unidades de temperatura, como Celsius a Fahrenheit.
import time
from os import system

def limpiarConsola():
    """
    Función que espera 2 segundos y luego limpia la consola.
    """
    time.sleep(0.5)
    system("cls")

def celsiusFahrenheit(temperatura,tipo):
    """
    Devuelve la conversion de temperatura dependiendo el tipo.
    Si Tipo == 'c' convierte Celsius a Fahrenheit
    Si es 'f' convierte Fahrenhit a Celsius

    Args:
        temperatura (_type_): La cantidad de grados de la temperatura
        tipo (_type_): Tipo de conversion

    Returns:
        _type_: Devuelve la temperatura
    """
    if tipo == "c":
        x = (temperatura * 9/5)+32
    elif tipo == "f":
        x = (temperatura-32) * 5/9

    return x

def longitud(longitud,tipo):
    if tipo == "pm": #Pies a metros
        x = (longitud / 3.281)
    elif tipo == "mp": #Metros a pies
        x = (longitud * 3.281)
    elif tipo == "km": #Kilómetros a metros
        x = (longitud * 1000)
    elif tipo == "mk": #Metros a Kilómetros
        x = (longitud / 1000)
    elif tipo == "kp": #Kilómetros a pies
        x = (longitud * 3281)
    elif tipo == "pk": #Pies a Kilómetros
        x = (longitud / 3281)

    return x


def inicio():
    limpiarConsola()
    print("Esta app te va a ayudar a convertir tus unidades.")
    print("Que tipo de conversion deseas realizar?")
    print("Tienes las siguientes opciones: ")
    print("c = Celsius a Fahrenhit")    #
    print("f = Fahrenhit a Celsius")    #
    print("pm = Pies a metros") #
    print("mp = Metros a pies") #
    print("km = Kilómetros a metros")   #
    print("mk = Metros a Kilómetros")   #
    print("kp = Kilómetros a pies") #
    print("pk = Pies a Kilómetros") #
    print("e = Salir")
    opcion = input("Escriba la opcion: ").lower()

    if opcion == "c":
        temp = float(input("Escriba la temperatura en C°: "))
        print(f"{temp} C° equivalen en F° a: {celsiusFahrenheit(temp,opcion)}")
    elif opcion == "f":
        temp = float(input("Escriba la temperatura en F°: "))
        print(f"{temp} F° equivalen en C° a: {celsiusFahrenheit(temp,opcion)}")
    elif opcion == "pm":
        long = float(input("La longitud en pies: "))
        print(f"{long} pies equivalen en metros: {longitud(long,opcion)}")
    elif opcion == "mp":
        long = float(input("La longitud en metros: "))
        print(f"{long} metros equivalen en pies: {longitud(long,opcion)}")
    elif opcion == "km":
        long = float(input("La longitud en km: "))
        print(f"{long} km equivalen en metros: {longitud(long,opcion)}")
    elif opcion == "mk":
        long = float(input("La longitud en metros: "))
        print(f"{long} m equivalen en kilometros: {longitud(long,opcion)}")
    elif opcion == "kp":
        long = float(input("La longitud en kilometros: "))
        print(f"{long} km equivalen en pies: {longitud(long,opcion)}")
    elif opcion == "pk":
        long = float(input("La longitud en pies: "))
        print(f"{long} pies equivalen en km: {longitud(long,opcion)}")
    elif opcion == "e":
        exit()
    else:
        print("Ninguna opcion es valida.")

inicio()

