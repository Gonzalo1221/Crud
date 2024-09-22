# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .# Utiliza una imagen base de Python 3.12
FROM python:3.12

# Instala herramientas de desarrollo y dependencias necesarias para compilar paquetes
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala las dependencias necesarias para greenlet
RUN apt-get update && apt-get install -y build-essential \
    && pip install greenlet --only-binary=:all:

# Instala las dependencias de la aplicación desde el archivo requirements.txt
RUN pip install --disable-pip-version-check --upgrade -r requirements.txt

# Copia todo el contenido del directorio actual al contenedor
COPY . .

# Expone el puerto 5000 (o el puerto en el que se ejecute la aplicación Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]


# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copia todo el contenido del directorio actual al contenedor
COPY . .

# Expone el puerto 5000 (o el puerto en el que se ejecute tu aplicación Flask)
EXPOSE 5000

# Comando para ejecutar tu aplicación Flask
CMD ["python", "app.py"]
