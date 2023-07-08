# Laboratório de envio de arquivos entre máquinas distintas usando Docker

Este é um guia para executar um laboratório que envia arquivos entre máquinas distintas usando Docker. O laboratório consiste em um cliente que envia um arquivo para um servidor. É necessário realizar o download e o build dos arquivos em ambas as máquinas correspondentes.

## Pré-requisitos

- Docker instalado nas máquinas envolvidas.

## Passo a passo

1. Faça o download dos arquivos deste repositório em ambas as máquinas, cliente e servidor.

2. **Na máquina cliente**:
   - Entre no diretório "cliente" para montar o cliente que enviará os arquivos:
     ```
     sudo docker build -t client .
     ```
   - Execute o cliente que envia arquivos:
     ```
     sudo docker run -it --network host -v <endereço da pasta que contém o código client-http.py + arquivo que deseja ser enviado>:/app client:latest
     ```
     Substitua `<endereço da pasta que contém o código client-http.py + arquivo que deseja ser enviado>` pelo caminho da pasta que contém o arquivo `client-http.py` e o arquivo que você deseja enviar.

3. **Na máquina servidor**:
   - Entre no diretório "servidor" para montar o servidor que receberá os arquivos:
     ```
     sudo docker build -t server .
     ```
   - Execute o servidor que recebe arquivos:
     ```
     sudo docker run -it --network host -v <endereço que deseja receber os arquivos>:/root/receber server:latest
     ```
     Substitua `<endereço que deseja receber os arquivos>` pelo caminho onde deseja receber os arquivos no servidor.

     Observação: O código solicitará que você informe um novo nome para o arquivo a ser salvo, mas tome cuidado com a extensão do arquivo.

## Imagens Docker disponíveis no Docker Hub

Você também pode obter as imagens diretamente do Docker Hub usando os seguintes comandos:

- Para obter a imagem do cliente:

docker pull antonioentringer/client:latest

- Para obter a imagem do servidor:

docker pull antonioentringer/server:latest

Certifique-se de ter as imagens necessárias disponíveis localmente ou no Docker Hub para executar o laboratório com sucesso.

Lembre-se de que este guia é apenas um resumo do processo. Certifique-se de ler e entender o código e os arquivos do laboratório antes de executá-lo.
