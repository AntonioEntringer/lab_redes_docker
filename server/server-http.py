from flask import Flask, request
import os

app = Flask(__name__)

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados)

@app.route('/upload', methods=['POST'])
def receber_arquivo():
    arquivo = request.files['arquivo']
    nome_arquivo = arquivo.filename

    dados = arquivo.read()
    
    # Criar o diretório /root/receber se ele não existir
    diretorio_salvar = '/root/receber'
    if not os.path.exists(diretorio_salvar):
        os.makedirs(diretorio_salvar)

    # Solicitar o nome do arquivo para salvar
    print("Cuidado: a extensão do novo nome de arquivo é diferente da original.")
    novo_nome = input("Digite o novo nome do arquivo: ")
    
    # Verificar a extensão do novo nome de arquivo
    extensao = os.path.splitext(novo_nome)[1]      
    
    # Salvar o arquivo com o novo nome
    salvar_arquivo(os.path.join(diretorio_salvar, novo_nome), dados)
    return "Arquivo {} recebido e salvo com sucesso.".format(nome_arquivo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

