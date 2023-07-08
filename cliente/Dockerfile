# Use a imagem base do Python Slim
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo Python para o diretório de trabalho do contêiner
COPY cliente-http.py /app
COPY image-stitching.git /app
# Instala a dependência do Python (requests)
RUN pip install --no-cache-dir requests

# Define o comando de inicialização do contêiner
CMD [ "python", "cliente-http.py" ]

