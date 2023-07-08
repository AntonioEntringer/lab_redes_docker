# Laboratório de envio de arquivos entre máquinas distintas usando Docker

Este é um guia para executar um laboratório que envia arquivos entre máquinas distintas usando Docker. O laboratório consiste em um cliente que envia um arquivo para um servidor. É necessário realizar o download e a construção dos arquivos em ambas as máquinas correspondentes.

## Pré-requisitos

- Docker instalado nas máquinas envolvidas.

## Passo a passo

1. Faça o download dos arquivos deste repositório em ambas as máquinas, cliente e servidor.

2. **Na máquina cliente**:
   - Entre no diretório "cliente" para construir o cliente que enviará os arquivos:
     ```
     sudo docker build -t client .
     ```
   - Execute o cliente que envia arquivos:
     ```
     sudo docker run -it --network host -v <caminho da pasta que contém o código client-http.py + arquivo que deseja ser enviado>:/app client:latest
     ```
     Substitua `<caminho da pasta que contém o código client-http.py + arquivo que deseja ser enviado>` pelo caminho da pasta que contém o arquivo `client-http.py` e o arquivo que você deseja enviar.

3. **Na máquina servidor**:
   - Entre no diretório "servidor" para construir o servidor que receberá os arquivos:
     ```
     sudo docker build -t server .
     ```
   - Execute o servidor que recebe arquivos:
     ```
     sudo docker run -it --network host -v <caminho onde deseja receber os arquivos>:/root/receber server:latest
     ```
     Substitua `<caminho onde deseja receber os arquivos>` pelo caminho onde você deseja receber os arquivos no servidor.

     Observação: O código solicitará que você informe um novo nome para o arquivo a ser salvo, mas tome cuidado com a extensão do arquivo.

## Imagens Docker disponíveis no Docker Hub

Você também pode obter as imagens diretamente do Docker Hub usando os seguintes comandos:

- Para obter a imagem do cliente:
