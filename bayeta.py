
#Autor: Javier Mazza Martin

import random

# Funcion frotar
def frotar(n_frases: int = 1) -> list():

    frases_elegidas = []

    with open('frases.txt', 'r') as archivo:
        frases_disponibles = archivo.readlines()

    for i in range(min(n_frases, len(frases_disponibles))):
            frase_elegida = random.choice(frases_disponibles)
            if(frase_elegida in frases_elegidas):
                 i -= 1
            else:
                frases_elegidas.append(frase_elegida.strip())  # Eliminar el salto de línea

    return frases_elegidas
