"""
Día 3: Contador de Palabras
Escribe un programa que tome un texto como entrada y cuente cuántas veces aparece cada palabra. Puedes usar diccionarios para mantener el conteo.
"""

def contadorPalabras(texto):
    """
    Le paso un texto, y lo que hago es separar el texto con split()
    recorro el texto, y cuento cuanats veces aparece la palabra en el mismo.
    Nueva vez que recorro una palabra la guardo en una lista, para que si aparece la palabra de nuevo, no tengo que volver a contarla

    Args:
        texto (str): Texto a reccorer
    """
    texto = texto.split()
    textocontado = []
    for i in texto:
        if i not in textocontado:
            x = texto.count(i)
            print(f"La palabra '{i}' aparece: {x}")
        textocontado.append(i)


contadorPalabras(input("Escriba el texto a contar: "))