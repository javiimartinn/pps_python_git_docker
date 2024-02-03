#---Fase de resolución de dependencias---#
FROM python:slim as builder

# Se establece el directorio de trabajo
WORKDIR /app

# Se copia el archivo de requisitos
COPY requirements .

# Se actualiza pip
RUN pip install --upgrade pip

# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements


#---Fase de ejecución---#
FROM builder as runner

# Se copia el código fuente
COPY . .

# Se establece el comando predeterminado
CMD ["python", "app.py"]
