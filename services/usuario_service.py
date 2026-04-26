class UsuarioService:
    def __init__(self, storage):
        self.storage = storage

    def registrar_usuario(self):
        usuarios = self.storage.carregar()

        print("\n--- Registro de Usuário ---")
        nome = input("Digite o nome de usuário: ")

        if nome in usuarios:
            print("Erro: Usuário já existe!")
            return

        senha = input("Digite a senha: ")
        usuarios[nome] = senha

        self.storage.salvar(usuarios)
        print(f"Usuário {nome} registrado com sucesso!")

    def fazer_login(self):
        usuarios = self.storage.carregar()

        print("\n--- Login ---")
        nome = input("Usuário: ")
        senha = input("Senha: ")

        if nome in usuarios and usuarios[nome] == senha:
            print("Acesso concedido! Bem-vindo ao sistema.")
        else:
            print("Usuário ou senha incorretos.")