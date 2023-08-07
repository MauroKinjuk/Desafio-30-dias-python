#Día 4: Lista de Tareas
#Crea una aplicación de lista de tareas donde puedas agregar, eliminar y marcar tareas como completadas. 
#Puedes usar una estructura de datos como una lista o un archivo para almacenar las tareas.

import msvcrt   #Para detectar teclas presionadas
from os import system   #Para poder limpiar la consola
import time #Para poder esperar un tiempo

archivoDeTexto = "Archivos/tareas.txt"

def limpiarConsola():
    """
    Función que espera 2 segundos y luego limpia la consola.
    """
    time.sleep(0.5)
    system("cls")

def agregarTareas():
    """
    Agrega tareas al archivo tareas.txt
    Para esto, abre el archivo y espera un input del texto que se desea agregar.
    Luego agrega un fin de linea, llama a la función para limpiar la consola, y vuelve al inicio.
    """
    limpiarConsola()
    with open(archivoDeTexto, "a") as archivo:
        x = input("Escribe la tarea que desear agregar: ")
        archivo.write(x + "     | Incompleta |" + "\n")
    print("Tarea agregada exitosamente.")
    limpiarConsola()
    inicio()

def verTareas():
    """
    Imprime el contenido del archivo tareas.txt
    Lo que hago es abrir el archivo, guardar sus lineas en la variable 'lineas'
    Y después recorro esta variable, y le asigno un numero con enumerate
    """
    print("Estas son las tareas que tienes actualmente: ")
    with open(archivoDeTexto,'r') as archivo:
        lineas = archivo.readlines()
        for i,tarea in enumerate(lineas):
            print(f"{i} - {tarea.strip()}")


def marcarCompleta():
    """
    Primeramente muestra todas las tareas actualmente.
    Pide que se marque el numero de la tarea a completar.
    Luego genera una lista de esas tareas, y con un for las recorre, cuando encuentra el numero de la tarea, reemplaza 'Incompleta' por 'Completa'
    """
    verTareas()
    nTarea = input("Escribe el numero de tarea que deseas marcar como completa: ")

    with open(archivoDeTexto,"r") as archivo:
        lineas = archivo.readlines() 

    with open(archivoDeTexto,"w") as archivo:
        for numero, linea in enumerate(lineas):
            if numero == int(nTarea):
                x = linea.replace("Incompleta","Completa")
                archivo.writelines(x)
            else:
                archivo.writelines(linea)
    print("La tarea se completó correctamente.")
    limpiarConsola()
    inicio()

def borrarTareas():
    limpiarConsola()
    #Guardo en una lista lo que tengo actualmente en el archivo
    with open(archivoDeTexto,'r') as archivo:
        lineas = archivo.readlines()

    verTareas() 

    numerABorrar = input("Escribe la tarea a borrar: ")
    with open(archivoDeTexto,'w') as archivo:
        for numero, linea in enumerate(lineas):
            if numero != int(numerABorrar):
                archivo.writelines(linea)

    print("Tarea borrada exitosamente.")
    limpiarConsola()
    inicio()

def inicio():
    print("Este es tu gestor de tareas pendientes.")
    print("Que deseas hacer? (Presiona la tecla)")
    print("a: Agregar tareas")
    print("v: Ver tareas")
    print("s: Completar tarea")
    print("b: Borrar tareas")
    print("e: Salir")
    opcion = msvcrt.getwch().lower()

    if opcion == "a":
        agregarTareas()
    if opcion == 'v':
        verTareas()
    if opcion == 's':
        marcarCompleta()
    if opcion == 'b':
        borrarTareas()
    if opcion == "e":
        print("Que tengas un buen dia!")
        limpiarConsola()
        exit()

inicio()