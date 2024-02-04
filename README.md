# Bayeta de la Fortuna
Repositorio que contiene la primera tarea del segundo tema de Puesta en Producción Segura.

## Descripcion de la aplicacion:
La aplicacion se llama "Bayeta de la Fortuna", y consiste en un programa cuya funcionalidad esta inspirada en las Galletas de la Fortuna, devolviendo mensajes curiosos cuando se ejecute.

Los ficheros principales de la aplicacion son:

- app.py: es el fichero principal, que crea una aplicación web utilizando la librería Flask. Para ejecutar la aplicación primero hay que acceder al entorno y después ejecutar el comando “python3 app.py”.
    
    Para poder visualizarla es necesario acceder al navegador y acceder a la dirección "http://127.0.0.1:5000". Para usar la funcion de la aplicacion que muestra las frases de las galletas, hay que acceder a la direccion "http://127.0.0.1:5000/frotar/4".


- bayeta.py: es un fichero que contiene el metodo "frotar" que accede al fichero prueba_mongo y obtiene las frases de la base de datos.


- prueba_mongo: es el fichero que contiene todo lo relacionado con la conexión a la base de datos. 
    
    Se divide en tres funciones principales: una de instanciación, que abre la conexion, una de inicializacion que agrega los datos almacenados en un fichero a la base (si hiciera falta) y una para realizar la consulta.

## Detalles del despliegue de la aplicacion:

### Creación de un nuevo entorno para la ejecución:
-Con el comando "python3 -m venv Nombre-Entorno" y se puede acceder al mismo con el comando "source Nombre-Entorno/bin/activate". Para desactivar el entorno basta con ejecutar el comando "deactivate".

### Resolver Dependencias del proyecto:
-Para resolver las dependencias primero el nuevo usuario tiene acceder a su entorno, y desde ahí hay que ejecutar el comando “pip install -r requirements *” que sirve para importar las dependencias del fichero “requirements” presente en el fichero raíz del proyecto.

### Creación de Imagen Docker:
-Para poder ejecutar la aplicación en un contenedor de docker primero se necesita una imagen, que se puede crear utilizando el Dockerfile presente en el repositorio. Ejecutando el comando "docker build -t nombre_imagen ." se puede crear la imagen.

### Creación de Contenedor Docker:
-Para desplegar un contenedor hay que ejecutar el comando "docker run 'nombre_imagen'", y una vez creado para arrancarlo hay que ejecutar el comando "docker start 'nombre_contenedor'", y para acceder al mismo hay que ejecutar el comando "docker exec -it 'container_id_or_name' /bin/bash".

## Entorno de Ejecución:
-Se ha creado un fichero docker-compose.yml, con el cual se pueden tanto crear comom iniciar contenedores de docker. Con el comando "docker compose up -d" se pueden iniciar los contenedores indicados en el fichero .yml (en este caso tanto el contenedor que contiene la aplicacion como el que contiene la base de datos).