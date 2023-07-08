import requests

def enviar_arquivo(nome_arquivo, endereco_servidor, porta_servidor):
    url = f"http://{endereco_servidor}:{porta_servidor}/upload"

    with open(nome_arquivo, 'rb') as arquivo:
        response = requests.post(url, files={'arquivo': arquivo})

    if response.status_code == 200:
        print("Arquivo enviado com sucesso.")
    else:
        print("Ocorreu um erro ao enviar o arquivo.")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo que deseja enviar: ")
    endereco_servidor = input("Digite o endereço IP do servidor: ")
    print('Press CTRL+C to quit')
    porta_servidor = 5001

    enviar_arquivo(nome_arquivo, endereco_servidor, porta_servidor)

