import json
import os

FILE_PATH = "usuarios.json"
EVENTOS_FILE = "eventos.json"

# ==========================================
# --- CLASSES (OOP - Card 7) ---
# ==========================================

class Evento:
    def __init__(self, nome, data, preco, total_bilhetes, vendidos=0, check_ins=0):
        self.nome = nome
        self.data = data
        self.preco = float(preco)
        self.total_bilhetes = int(total_bilhetes)
        self.vendidos = int(vendidos)
        self.check_ins = int(check_ins)

    @property
    def vagas(self):
        return self.total_bilhetes - self.vendidos

    def to_dict(self):
        return {
            "data": self.data,
            "preco": self.preco,
            "total_bilhetes": self.total_bilhetes,
            "vendidos": self.vendidos,
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
            # Converte os dicionários do JSON em Objetos da Classe Evento
            return {nome: Evento(nome, **info) for nome, info in dados.items()}

    def salvar_eventos(self):
        # Converte os Objetos de volta para dicionários antes de salvar no JSON
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
        print("\n--- Cadastro de Novo Evento ---")
        nome = input("Nome do Evento: ")
        data = input("Data (DD/MM/AAAA): ")
        try:
            preco = float(input("Preço do Bilhete (€): "))
            quantidade = int(input("Quantidade de Bilhetes disponíveis: "))
            
            # Instanciando um novo objeto Evento
            novo_evento = Evento(nome, data, preco, quantidade)
            self.eventos[nome] = novo_evento
            self.salvar_eventos()
            print(f"Evento '{nome}' cadastrado com sucesso!")
        except ValueError:
            print("Erro: Preço e Quantidade devem ser números!")

    def listar_eventos(self):
        print("\n--- Lista de Eventos Cadastrados ---")
        if not self.eventos:
            print("Nenhum evento cadastrado no momento.")
            return False
        
        for nome, evento in self.eventos.items():
            print(f"- {evento.nome} | Data: {evento.data} | Preço: {evento.preco}€ | Vagas: {evento.vagas}")
        return True

    def editar_evento(self):
        print("\n--- Atualizar Evento ---")
        if not self.listar_eventos():
            return

        nome = input("\nDigite o nome do evento que deseja editar: ")
        if nome in self.eventos:
            evento = self.eventos[nome]
            print("Dica: Deixe em branco e pressione Enter para manter o valor atual.")
            evento.data = input(f"Nova data ({evento.data}): ") or evento.data
            
            try:
                novo_preco_str = input(f"Novo preço ({evento.preco}€): ")
                evento.preco = float(novo_preco_str) if novo_preco_str else evento.preco
                self.salvar_eventos()
                print("✅ Evento atualizado com sucesso!")
            except ValueError:
                print("❌ Erro: O preço deve ser um número!")
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

        nome_evento = input("\nDigite o nome do evento para o qual deseja comprar bilhete: ")
        if nome_evento in self.eventos:
            evento = self.eventos[nome_evento]
            if evento.vagas > 0:
                confirmar = input(f"O bilhete para '{evento.nome}' custa {evento.preco}€. Deseja confirmar a compra? (s/n): ")
                if confirmar.lower() == 's':
                    evento.vendidos += 1
                    self.salvar_eventos()
                    print(f"\033[92m✅ Compra realizada com sucesso!\033[0m")
                    print(f"🎫 O seu código de entrada (QR Code) é: {evento.nome}")
                else:
                    print("Compra cancelada.")
            else:
                print("\033[91m❌ Desculpe, os bilhetes para este evento estão esgotados!\033[0m")
        else:
            print("❌ Evento não encontrado.")

    # --- Módulo Staff ---
    def validar_bilhete(self):
        print("\n--- 🎫 Validação de Bilhetes (Área Staff) ---")
        codigo = input("Escaneie o QR Code ou digite o código do bilhete: ")
        
        if codigo in self.eventos:
            evento = self.eventos[codigo]
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
        evento_mais_popular = None
        max_vendidos = -1

        for nome, evento in self.eventos.items():
            receita_evento = evento.vendidos * evento.preco
            total_receita += receita_evento
            total_bilhetes_vendidos += evento.vendidos
            
            if evento.vendidos > max_vendidos:
                max_vendidos = evento.vendidos
                evento_mais_popular = nome
            
            ocupacao = (evento.check_ins / evento.vendidos * 100) if evento.vendidos > 0 else 0
            
            print(f"📍 {nome}:")
            print(f"   - Receita: {receita_evento:.2f}€")
            print(f"   - Check-ins: {evento.check_ins} de {evento.vendidos} ({ocupacao:.1f}%)")

        print("="*40)
        print(f"💰 RECEITA TOTAL: {total_receita:.2f}€")
        print(f"🎟️ TOTAL DE BILHETES: {total_bilhetes_vendidos}")
        print(f"🌟 EVENTO MAIS POPULAR: {evento_mais_popular}")
        print("="*40)

    # --- Menu Principal ---
    def executar(self):
        while True:
            print("\n" + "="*30)
            print("🎫 SISTEMA DE BILHETERIA (OOP)")
            print("="*30)
            print("1. Registrar Utilizador")
            print("2. Login")
            print("3. Cadastrar Evento (Organizador/Create)")
            print("4. Listar Eventos (Read)")
            print("5. Editar Evento (Organizador/Update)")
            print("6. Excluir Evento (Organizador/Delete)")
            print("7. Comprar Bilhete (Cliente)")
            print("8. Validar Bilhete (Staff/Check-in)") 
            print("9. Dashboard de Vendas (Organizador)")
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