import json
import os

FILE_PATH = "usuarios.json"
EVENTOS_FILE = 'eventos.json'

def pedir_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Erro: Por favor, digite apenas números!")
        return None

def carregar_usuarios():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(FILE_PATH, 'w') as f:
        json.dump(usuarios, f, indent=4)

def registrar_usuario():
    usuarios = carregar_usuarios()
    print("\n--- Registro de Usuário ---")
    nome = input("Digite o nome de usuário: ")
    if nome in usuarios:
        print("Erro: Usuário já existe!")
        return
    senha = input("Digite a senha: ")
    usuarios[nome] = senha
    salvar_usuarios(usuarios)
    print(f"Usuário {nome} registrado com sucesso!")

def fazer_login():
    usuarios = carregar_usuarios()
    print("\n--- Login ---")
    nome = input("Usuário: ")
    senha = input("Senha: ")
    
    if nome in usuarios and usuarios[nome] == senha:
        print("Acesso concedido! Bem-vindo ao sistema.")
    else:
        print("Usuário ou senha incorretos.")

def cadastrar_evento():
    eventos = carregar_eventos()
    print("\n--- Cadastro de Novo Evento ---")
    nome = input("Nome do Evento: ")
    data = input("Data (DD/MM/AAAA): ")
    
    try:
        preco = float(input("Preço do Bilhete (€): "))
        quantidade = int(input("Quantidade de Bilhetes disponíveis: "))
        
        eventos[nome] = {
            "data": data,
            "preco": preco,
            "total_bilhetes": quantidade,
            "vendidos": 0
        }
        
        salvar_eventos(eventos)
        print(f"Evento '{nome}' cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Preço e Quantidade devem ser números!")

def carregar_eventos():
    if not os.path.exists(EVENTOS_FILE):
        return {}
    with open(EVENTOS_FILE, 'r') as f:
        return json.load(f)

def salvar_eventos(eventos):
    with open(EVENTOS_FILE, 'w') as f:
        json.dump(eventos, f, indent=4)

if __name__ == "__main__":
    while True:
        print("\n1. Registrar Utilizador\n2. Login\n3. Cadastrar Evento (Organizador)\n4. Sair")
        opcao = pedir_opcao()
        
        if opcao is None: 
            continue
            
        if opcao == 1: registrar_usuario()
        elif opcao == 2: fazer_login()
        elif opcao == 3: cadastrar_evento()
        elif opcao == 4: break