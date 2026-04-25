class EventoService:
    def __init__(self, storage):
        self.storage = storage

    def cadastrar_evento(self):
        eventos = self.storage.carregar()

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

            self.storage.salvar(eventos)
            print(f"Evento '{nome}' cadastrado com sucesso!")

        except ValueError:
            print("Erro: Preço e Quantidade devem ser números!")

    def listar_eventos(self):
        print("\n--- Lista de Eventos Cadastrados ---")
        eventos = self.storage.carregar()

        if not eventos:
            print("Nenhum evento cadastrado no momento.")
            return

        for nome, info in eventos.items():
            vagas = info["total_bilhetes"] - info["vendidos"]
            print(f"- {nome} | Data: {info['data']} | Preço: {info['preco']}€ | Vagas: {vagas}")

    def editar_evento(self):
        print("\n--- Atualizar Evento ---")
        eventos = self.storage.carregar()

        self.listar_eventos()

        if not eventos:
            return

        nome = input("\nDigite o nome do evento que deseja editar: ")

        if nome in eventos:
            print("Dica: Deixe em branco e pressione Enter para manter o valor atual.")

            nova_data = input(f"Nova data ({eventos[nome]['data']}): ") or eventos[nome]["data"]

            try:
                novo_preco_str = input(f"Novo preço ({eventos[nome]['preco']}€): ")
                novo_preco = float(novo_preco_str) if novo_preco_str else eventos[nome]["preco"]

                eventos[nome]["data"] = nova_data
                eventos[nome]["preco"] = novo_preco

                self.storage.salvar(eventos)
                print("✅ Evento atualizado com sucesso!")

            except ValueError:
                print("❌ Erro: O preço deve ser um número!")
        else:
            print("❌ Evento não encontrado.")

    def excluir_evento(self):
        print("\n--- Excluir Evento ---")
        eventos = self.storage.carregar()

        self.listar_eventos()

        if not eventos:
            return

        nome = input("\nDigite o nome do evento que deseja apagar: ")

        if nome in eventos:
            confirmar = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ")

            if confirmar.lower() == "s":
                del eventos[nome]
                self.storage.salvar(eventos)
                print("✅ Evento excluído permanentemente!")
        else:
            print("❌ Evento não encontrado.")