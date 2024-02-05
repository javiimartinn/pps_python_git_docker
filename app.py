
# Autor: Javier Mazza Martin

# Importaciones
from bayeta import frotar, agregar_frases
from flask import Flask, jsonify, request

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

#Funciones:
#Funcion saludar
@app.route('/')
def saludar():
    return '¡Hola, mundo2!'


#Funcion frotar
@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    # Llama a la función frotar y obtén las frases
    frases = frotar(n_frases)
    
    # Devuelve las frases en formato JSON
    return jsonify({'frases': frases})


# Función para añadir frases
@app.route('/frotar/add', methods=['POST'])
def add_frases():
    # Obtiene los datos JSON enviados en la solicitud
    data = request.get_json()
    
    # Verifica que se hayan proporcionado datos
    if not data:
        return jsonify({'error': 'No se proporcionaron datos JSON'}), 400
    
    # Verifica que se hayan proporcionado frases para añadir
    if 'frases' not in data or not isinstance(data['frases'], list):
        return jsonify({'error': 'Formato de datos incorrecto'}), 400
    
    # Llama a la función de la aplicación para añadir las frases
    if(agregar_frases(data['frases']) == True):
        # Devuelve una respuesta exitosa
        return jsonify({'message': 'Frases añadidas correctamente'}), 200
    else:
        # Devuelve una respuesta de error
        return jsonify({'message': 'Error al agregar las Frases'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0') # Es necesario declarar el host='0.0.0.0', ya que las aplicaciones Flask lo requieren para
                            # ser lanzadas desde un contenedor.
