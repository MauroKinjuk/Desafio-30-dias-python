#Segundo dia: Generador de contraseñas

import random

def generador(n1:int):
    """
    De unas listas de caracteres, se genera una lista combinada.
    Luego usa la funcion random.choice seleccionar palabras al azar y concatenarlas en un string
    Usa el parametro n1 para determinar el largo de la contraseña

    Args:
        n1 (int): Es el largo de la contraseña elegida
    """
    
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letrasMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = [0,1,2,3,4,5,6,7,8,9]
    especiales = ['!','#','$','%','&']
    combinado = letras+numeros+especiales+letrasMayus
    x = ""
    for i in range(int(n1)):
        x += str(random.choice(combinado))
    return(x)

def iniciar():
    print("Hola! Vamos a generar una contraseña segura para lo que necesites")
    print("Esta contraseña contendrá letras mayúsculas, minúsculas, números y caracteres especiales.")
    while True:
        try:
            x = int(input("Que tan grande deseas la contraseña? (Se recomienda una de 8 hacia arriba): "))
            break
        except ValueError: print("Debe ser un numero entero")
    
    print("Tu contraseña es: " + generador(x))


iniciar()