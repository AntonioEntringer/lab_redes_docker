Execução de um laboratório que envia arquivos entre maquinas distintas usando Docker

faça donwload dos arquivos desse git

#maquina client envia arquivo
#maquina server recebe arquivo de qualquer client

#entre no diretório cliente para montar o arquivo
#Montar o cliente que envia arquivos
sudo docker build -t client .

#Executar o cliente que envia arquivos
sudo docker run -it --network host -v <endereço da pasta que contenha o codigo client-http.py + arquivo que deseja ser enviado>:/app client:latest

#Entre no diretório server na maquina que será o servidor
#Montar o cliente que recebe arquivos
sudo docker build -t server .

#Executar o server que recebe arquivos
sudo docker run -it --network host -v <endereço que deseja receber os arquivos>:/root/receber server:latest
#O codigo vai pedir para informar um novo nome para o arquivo ser salvo, MAS DEVE SER TOMADO CUIDADOS COM A EXTENÇÃO 

<><><><><><><><><><><><><><><>DOCKER<><><><><><><><><><><><><><><><><>

Imagens disponiveis no dockerhub por meio de:

docker pull antonioentringer/client:latest

docker pull antonioentringer/server:latest
