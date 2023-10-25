# Utiliza una imagen base de Ubuntu (puedes elegir otra imagen base si prefieres)
FROM ubuntu:20.04

# Instala MongoDB
RUN apt-get update && apt-get install -y mongodb

# Crea un directorio para almacenar los datos de MongoDB
RUN mkdir -p /data/db

# Expone el puerto por defecto de MongoDB
EXPOSE 27017

# Inicia el servicio de MongoDB cuando se inicia el contenedor
CMD ["mongod"]
