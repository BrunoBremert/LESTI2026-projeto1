import json
import os

FILE_PATH = "usuarios.json"

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

if __name__ == "__main__":
    while True:
        opcao = input("\n1. Registrar\n2. Login\n3. Sair\nEscolha: ")
        if opcao == '1': registrar_usuario()
        elif opcao == '2': fazer_login()
        elif opcao == '3': break