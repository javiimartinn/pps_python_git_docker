
# Autor: Javier Mazza Martin

# Importaciones
from bayeta import frotar
from flask import Flask, jsonify

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

#Funciones:
#Funcion saludar
@app.route('/')
def saludar():
    return '¡Hola, mundo!'

#Funcion frotar
@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    # Llama a la función frotar y obtén las frases
    frases = frotar(n_frases)
    
    # Devuelve las frases en formato JSON
    return jsonify({'frases': frases})

if __name__ == '__main__':
    app.run()
