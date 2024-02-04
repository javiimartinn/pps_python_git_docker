from pymongo import MongoClient

# Dirección IP del servidor mongodb:
ip_server_mongo = '172.0.0.3'

# Conexión con el motor de Mongo
cliente_mongo = MongoClient('mongodb://' + ip_server_mongo + ':27017/')


# Funciones: #
# Instanciación (conexión con el motor, obtener la BBDD y la colección concreta)
def instanciar():
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con  la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']

    return frases_auspiciosas


# Inicialización (insertar datos, si procede). No haremos uso de lista de datos, sino de un fichero.
def inicializar(frases_auspiciosas):
    # Inserción de datos
    with open('frases.txt', 'r') as archivo:
        frases_disponibles = [{"frase": line.strip()} for line in archivo]
    frases_auspiciosas.insert_many(frases_disponibles)
    

# Funcion que realiza la consulta a la base de datos
def consultar(n_frases: int):
    frases_auspiciosas = instanciar()

    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        inicializar(frases_auspiciosas)

    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))

    return frases_aleatorias


# Cerrar cliente
def cerrar_sesion():
    cliente_mongo.close()
