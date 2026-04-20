def registrar_usuario():
    print(" Registro de Usuário ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Aqui salvaríamos em um arquivo ou banco de dados
    print(f"Usuário {usuario} registrado com sucesso!\n")
    return {"usuario": usuario, "senha": senha}

def fazer_login(dados_registrados):
    print(" Login ")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == dados_registrados['usuario'] and senha == dados_registrados['senha']:
        print("Acesso concedido!")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    
    # Fluxo simples para teste
    user_db = registrar_usuario()
    fazer_login(user_db)