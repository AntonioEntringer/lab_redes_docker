# Use uma imagem base do Python
FROM python:3.8.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o código Python para o diretório de trabalho do contêiner
COPY server-http.py /app

# Instala a dependência do Python
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir flask

# Define o comando de inicialização do contêiner
CMD [ "python", "server-http.py" ]

