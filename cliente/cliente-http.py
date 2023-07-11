import requests
import os

def listar_arquivos(pasta):
    arquivos = os.listdir(pasta)
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")
    return arquivos

def enviar_arquivo(nome_arquivo, endereco_servidor, porta_servidor):
    url = f"http://{endereco_servidor}:{porta_servidor}/upload"

    with open(nome_arquivo, 'rb') as arquivo:
        response = requests.post(url, files={'arquivo': arquivo})

    if response.status_code == 200:
        print("Arquivo enviado com sucesso.")
    else:
        print("Ocorreu um erro ao enviar o arquivo.")

if __name__ == "__main__":
    pasta = '/root/enviar'
    arquivos = listar_arquivos(pasta)

    while True:
        numero_arquivo = input("Digite o número do arquivo que deseja enviar (ou 'q' para sair): ")
        if numero_arquivo == 'q':
            break

        try:
            indice = int(numero_arquivo) - 1
            nome_arquivo = arquivos[indice]
            endereco_servidor = input("Digite o endereço IP do servidor: ")
            porta_servidor = 5001

            enviar_arquivo(os.path.join(pasta, nome_arquivo), endereco_servidor, porta_servidor)
        except (ValueError, IndexError):
            print("Número inválido. Tente novamente.")
