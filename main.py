from storage.json_storage import JsonStorage
from services.usuario_service import UsuarioService
from services.evento_service import EventoService
from services.bilhete_service import BilheteService

FILE_PATH = "usuarios.json"
EVENTOS_FILE = "eventos.json"

# ==========================================
# --- CLASSES (OOP - Card 7 & Card 17) ---
# ==========================================

class Evento:
    def __init__(self, nome, data, preco=None, total_bilhetes=None, vendidos=0, check_ins=0, setores=None):
        self.nome = nome
        self.data = data
        self.check_ins = int(check_ins)
        
        # Lógica de migração: se o evento é antigo (não tem setores), criamos um setor "Geral" padrão
        if setores is not None:
            self.setores = setores
        else:
            self.setores = {
                "Geral": {
                    "preco": float(preco) if preco else 0.0,
                    "capacidade": int(total_bilhetes) if total_bilhetes else 0,
                    "vendidos": int(vendidos) if vendidos else 0
                }
            }

    @property
    def total_bilhetes(self):
        return sum(s["capacidade"] for s in self.setores.values())

    @property
    def vendidos(self):
        return sum(s["vendidos"] for s in self.setores.values())

    def to_dict(self):
        return {
            "data": self.data,
            "setores": self.setores,
            "check_ins": self.check_ins
        }


class SistemaBilheteria:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()
        self.eventos = self.carregar_eventos()

    # --- Persistência de Dados ---
    def carregar_usuarios(self):
        if not os.path.exists(FILE_PATH):
            return {}
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)

    def salvar_usuarios(self):
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.usuarios, f, indent=4)

    def carregar_eventos(self):
        if not os.path.exists(EVENTOS_FILE):
            return {}
        with open(EVENTOS_FILE, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return {nome: Evento(nome, **info) for nome, info in dados.items()}

    def salvar_eventos(self):
        dados = {nome: evento.to_dict() for nome, evento in self.eventos.items()}
        with open(EVENTOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)

    # --- Módulo de Usuários ---
    def registrar_usuario(self):
        print("\n--- Registro de Usuário ---")
        nome = input("Digite o nome de usuário: ")
        if nome in self.usuarios:
            print("Erro: Usuário já existe!")
            return
        senha = input("Digite a senha: ")
        self.usuarios[nome] = senha
        self.salvar_usuarios()
        print(f"Usuário {nome} registrado com sucesso!")

    def fazer_login(self):
        print("\n--- Login ---")
        nome = input("Usuário: ")
        senha = input("Senha: ")
        if nome in self.usuarios and self.usuarios[nome] == senha:
            print("Acesso concedido! Bem-vindo ao sistema.")
        else:
            print("Usuário ou senha incorretos.")

    # --- Módulo Organizador (CRUD) ---
    def cadastrar_evento(self):
        print("\n--- Cadastro de Novo Evento (Com Setores) ---")
        nome = input("Nome do Evento: ")
        data = input("Data (DD/MM/AAAA): ")
        
        setores = {}
        print("\nAdicione os setores do evento (ex: VIP, Plateia). Digite 'fim' no nome para terminar.")
        while True:
            nome_setor = input("\nNome do Setor (ou 'fim'): ")
            if nome_setor.lower() == 'fim':
                if not setores:
                    print("Erro: O evento precisa ter pelo menos um setor!")
                    continue
                break
            try:
                preco = float(input(f"Preço do bilhete para '{nome_setor}' (€): "))
                capacidade = int(input(f"Capacidade de lugares para '{nome_setor}': "))
                setores[nome_setor] = {
                    "preco": preco,
                    "capacidade": capacidade,
                    "vendidos": 0
                }
            except ValueError:
                print("Erro: Preço e Capacidade devem ser números!")
                
        novo_evento = Evento(nome, data, setores=setores)
        self.eventos[nome] = novo_evento
        self.salvar_eventos()
        print(f"\n✅ Evento '{nome}' cadastrado com sucesso com {len(setores)} setor(es)!")

    def listar_eventos(self):
        print("\n--- Lista de Eventos Cadastrados ---")
        if not self.eventos:
            print("Nenhum evento cadastrado no momento.")
            return False
        
        for nome, evento in self.eventos.items():
            print(f"\n📍 {evento.nome} | Data: {evento.data} | Lotação Total: {evento.vendidos}/{evento.total_bilhetes}")
            for nome_setor, info in evento.setores.items():
                vagas = info['capacidade'] - info['vendidos']
                print(f"   - Setor {nome_setor}: {info['preco']}€ | Vagas: {vagas}")
        return True

    def editar_evento(self):
        print("\n--- Atualizar Evento ---")
        if not self.listar_eventos():
            return

        nome = input("\nDigite o nome do evento que deseja editar a data: ")
        if nome in self.eventos:
            evento = self.eventos[nome]
            evento.data = input(f"Nova data ({evento.data}): ") or evento.data
            self.salvar_eventos()
            print("✅ Data do evento atualizada com sucesso! (Para editar setores, exclua e recrie o evento)")
        else:
            print("❌ Evento não encontrado.")

    def excluir_evento(self):
        print("\n--- Excluir Evento ---")
        if not self.listar_eventos():
            return

        nome = input("\nDigite o nome do evento que deseja apagar: ")
        if nome in self.eventos:
            confirmar = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ")
            if confirmar.lower() == 's':
                del self.eventos[nome]
                self.salvar_eventos()
                print("✅ Evento excluído permanentemente!")
        else:
            print("❌ Evento não encontrado.")

    # --- Módulo Cliente ---
    def comprar_bilhete(self):
        print("\n--- 🛒 Comprar Bilhete (Área Cliente) ---")
        if not self.listar_eventos():
            return

        nome_evento = input("\nDigite o nome do evento: ")
        if nome_evento in self.eventos:
            evento = self.eventos[nome_evento]
            nome_setor = input("Digite o nome do setor que deseja comprar: ")
            
            if nome_setor in evento.setores:
                setor = evento.setores[nome_setor]
                vagas = setor['capacidade'] - setor['vendidos']
                
                if vagas > 0:
                    confirmar = input(f"O bilhete '{nome_setor}' custa {setor['preco']}€. Confirmar compra? (s/n): ")
                    if confirmar.lower() == 's':
                        setor['vendidos'] += 1
                        self.salvar_eventos()
                        print(f"\033[92m✅ Compra realizada com sucesso!\033[0m")
                        print(f"🎫 O seu código de entrada (QR Code) é: {evento.nome}-{nome_setor}")
                    else:
                        print("Compra cancelada.")
                else:
                    print("\033[91m❌ Desculpe, este setor está esgotado!\033[0m")
            else:
                print("❌ Setor não encontrado.")
        else:
            print("❌ Evento não encontrado.")

    # --- Módulo Staff ---
    def validar_bilhete(self):
        print("\n--- 🎫 Validação de Bilhetes (Área Staff) ---")
        codigo = input("Escaneie o QR Code (ex: NomeEvento-Setor) ou digite apenas o nome do evento: ")
        
        # Pega apenas a primeira parte do código se tiver um traço (NomeEvento-Setor -> NomeEvento)
        nome_evento = codigo.split('-')[0]
        
        if nome_evento in self.eventos:
            evento = self.eventos[nome_evento]
            if evento.check_ins < evento.vendidos:
                evento.check_ins += 1
                self.salvar_eventos()
                print("\033[92m✅ APROVADO: Bilhete validado com sucesso!\033[0m")
            else:
                print("\033[91m❌ ERRO: Bilhete já utilizado ou duplicado!\033[0m")
        else:
            print("❌ ERRO: Código/Evento inválido.")

    # --- Módulo Dashboard ---
    def exibir_dashboard(self):
        print("\n" + "="*40)
        print("📊 DASHBOARD DE VENDAS E OCUPAÇÃO")
        print("="*40)
        
        if not self.eventos:
            print("Nenhum dado disponível.")
            return

        total_receita = 0
        total_bilhetes_vendidos = 0

        for nome, evento in self.eventos.items():
            receita_evento = sum(s['vendidos'] * s['preco'] for s in evento.setores.values())
            total_receita += receita_evento
            total_bilhetes_vendidos += evento.vendidos
            
            ocupacao = (evento.check_ins / evento.vendidos * 100) if evento.vendidos > 0 else 0
            
            print(f"📍 {nome}:")
            print(f"   - Receita gerada: {receita_evento:.2f}€")
            print(f"   - Check-ins na porta: {evento.check_ins} de {evento.vendidos} vendidos ({ocupacao:.1f}%)")

        print("="*40)
        print(f"💰 RECEITA GLOBAL: {total_receita:.2f}€")
        print(f"🎟️ TOTAL DE BILHETES VENDIDOS: {total_bilhetes_vendidos}")
        print("="*40)

    # --- Menu Principal ---
    def executar(self):
        while True:
            print("\n" + "="*30)
            print("🎫 SISTEMA DE BILHETERIA (OOP)")
            print("="*30)
            print("1. Registrar Utilizador")
            print("2. Login")
            print("3. Cadastrar Evento (Com Setores)")
            print("4. Listar Eventos")
            print("5. Editar Evento (Apenas Data)")
            print("6. Excluir Evento")
            print("7. Comprar Bilhete")
            print("8. Validar Bilhete (Staff)") 
            print("9. Dashboard de Vendas")
            print("10. Sair")
            
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números!")
                continue
                
            if opcao == 1: self.registrar_usuario()
            elif opcao == 2: self.fazer_login()
            elif opcao == 3: self.cadastrar_evento()
            elif opcao == 4: self.listar_eventos()
            elif opcao == 5: self.editar_evento()
            elif opcao == 6: self.excluir_evento()
            elif opcao == 7: self.comprar_bilhete()
            elif opcao == 8: self.validar_bilhete() 
            elif opcao == 9: self.exibir_dashboard()
            elif opcao == 10: 
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = SistemaBilheteria()
    app.executar()
