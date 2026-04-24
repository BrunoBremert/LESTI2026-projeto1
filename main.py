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
    # Mantemos a versão com encoding que o Dominik sugeriu
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
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
            "vendidos": 0,
            "check_ins": 0  
        }
        
        salvar_eventos(eventos)
        print(f"Evento '{nome}' cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Preço e Quantidade devem ser números!")

def carregar_eventos():
    if not os.path.exists(EVENTOS_FILE):
        return {}
    with open(EVENTOS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_eventos(eventos):
    with open(EVENTOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(eventos, f, indent=4)

# ==========================================
# --- FUNÇÕES DO DOMINIK (CRUD) ---
# ==========================================

def listar_eventos():
    print("\n--- Lista de Eventos Cadastrados ---")
    eventos = carregar_eventos()
    if not eventos:
        print("Nenhum evento cadastrado no momento.")
        return
    
    for nome, info in eventos.items():
        vagas = info['total_bilhetes'] - info['vendidos']
        print(f"- {nome} | Data: {info['data']} | Preço: {info['preco']}€ | Vagas: {vagas}")

def editar_evento():
    print("\n--- Atualizar Evento ---")
    eventos = carregar_eventos()
    listar_eventos()
    
    if not eventos:
        return

    nome = input("\nDigite o nome do evento que deseja editar: ")
    if nome in eventos:
        print("Dica: Deixe em branco e pressione Enter para manter o valor atual.")
        nova_data = input(f"Nova data ({eventos[nome]['data']}): ") or eventos[nome]['data']
        
        try:
            novo_preco_str = input(f"Novo preço ({eventos[nome]['preco']}€): ")
            novo_preco = float(novo_preco_str) if novo_preco_str else eventos[nome]['preco']
            
            eventos[nome]['data'] = nova_data
            eventos[nome]['preco'] = novo_preco
            salvar_eventos(eventos)
            print("✅ Evento atualizado com sucesso!")
        except ValueError:
            print("❌ Erro: O preço deve ser um número!")
    else:
        print("❌ Evento não encontrado.")

def excluir_evento():
    print("\n--- Excluir Evento ---")
    eventos = carregar_eventos()
    listar_eventos()
    
    if not eventos:
        return

    nome = input("\nDigite o nome do evento que deseja apagar: ")
    if nome in eventos:
        confirmar = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ")
        if confirmar.lower() == 's':
            del eventos[nome]
            salvar_eventos(eventos)
            print("✅ Evento excluído permanentemente!")
    else:
        print("❌ Evento não encontrado.")

def validar_bilhete():
    print("\n--- 🎫 Validação de Bilhetes (Área Staff) ---")
    eventos = carregar_eventos()
    listar_eventos()
    
    if not eventos:
        return

    nome_evento = input("\nNome do evento para check-in: ")
    if nome_evento in eventos:
        evento = eventos[nome_evento]
        
        # Verifica se ainda há pessoas que compraram mas não entraram
        if evento['check_ins'] < evento['vendidos']:
            print(f"Evento: {nome_evento}")
            print(f"Estado: {evento['check_ins']} entradas de {evento['vendidos']} bilhetes vendidos.")
            
            confirmar = input("Confirmar entrada de +1 participante? (s/n): ")
            if confirmar.lower() == 's':
                # ATUALIZAÇÃO REAL DOS DADOS
                eventos[nome_evento]['check_ins'] += 1
                salvar_eventos(eventos)
                
                print(f"✅ Acesso AUTORIZADO! Check-in realizado com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("⚠️ Alerta: Todos os bilhetes vendidos para este evento já fizeram check-in!")
    else:
        print("❌ Erro: Evento não encontrado.")

# --- MENU ATUALIZADO ---

if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        print("🎫 SISTEMA DE BILHETERIA")
        print("="*30)
        print("1. Registrar Utilizador")
        print("2. Login")
        print("3. Cadastrar Evento (Create)")
        print("4. Listar Eventos (Read)")
        print("5. Editar Evento (Update)")
        print("6. Excluir Evento (Delete)")
        print("7. Validar Bilhete (Staff/Check-in)") # Nova Opção
        print("8. Sair")
        
        opcao = pedir_opcao()
        
        if opcao is None: 
            continue
            
        if opcao == 1: registrar_usuario()
        elif opcao == 2: fazer_login()
        elif opcao == 3: cadastrar_evento()
        elif opcao == 4: listar_eventos()
        elif opcao == 5: editar_evento()
        elif opcao == 6: excluir_evento()
        elif opcao == 7: validar_bilhete() # Chamada da tua função
        elif opcao == 8: 
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")