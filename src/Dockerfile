# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Actualiza pip a la última versión (opcional, pero recomendable)
RUN pip install --upgrade pip

# Instala las dependencias de la aplicación desde el requirements.txt
RUN pip install --disable-pip-version-check --upgrade -r requirements.txt

# Copia todo el contenido del directorio actual al contenedor
COPY . .

# Expone el puerto 5000 (o el puerto en el que se ejecute tu aplicación Flask)
EXPOSE 5000

# Comando para ejecutar tu aplicación Flask
CMD ["python", "app.py"]