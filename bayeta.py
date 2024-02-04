
#Autor: Javier Mazza Martin

from prueba_mongo import consultar, agregar_frases

# Funcion frotar
def frotar(n_frases: int = 1) -> list():
    frases_elegidas = consultar(n_frases)
    lista_frases = [frase['frase'] for frase in frases_elegidas]
    return lista_frases

# Funcion agregar
def agregar(nuevas_frases: list):
    # Devuelve true si se han agregado las nuevas frases y false si no.
    return agregar_frases(nuevas_frases)