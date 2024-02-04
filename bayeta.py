
#Autor: Javier Mazza Martin

from prueba_mongo import consultar

# Funcion frotar
def frotar(n_frases: int = 1) -> list():
    frases_elegidas = consultar(n_frases)
    lista_frases = [frase['frase'] for frase in frases_elegidas]
    return lista_frases
