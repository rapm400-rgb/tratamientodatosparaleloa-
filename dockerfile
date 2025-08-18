# Imagen base python
FROM python:3.10-slim

#Directorio de trabaji
WORKDIR /app

#copiar archivos
COPY . .

#Instalar dependecnias
RUN pip install --no-cache-dir -r requeriments.txt

#Exponer puerto
EXPOSE 8080

#Comando para ejecutar la app
CMD [ "python", "app.py" ]