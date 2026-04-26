class BilheteService:
    def __init__(self, storage, evento_service):
        self.storage = storage
        self.evento_service = evento_service

    def comprar_bilhete(self):
        print("\n--- 🛒 Comprar Bilhete (Área Cliente) ---")
        eventos = self.storage.carregar()

        self.evento_service.listar_eventos()

        if not eventos:
            return

        nome_evento = input("\nDigite o nome do evento para o qual deseja comprar bilhete: ")

        if nome_evento in eventos:
            evento = eventos[nome_evento]
            vagas = evento["total_bilhetes"] - evento["vendidos"]

            if vagas > 0:
                confirmar = input(
                    f"O bilhete para '{nome_evento}' custa {evento['preco']}€. "
                    "Deseja confirmar a compra? (s/n): "
                )

                if confirmar.lower() == "s":
                    eventos[nome_evento]["vendidos"] += 1
                    self.storage.salvar(eventos)

                    print("\033[92m✅ Compra realizada com sucesso!\033[0m")
                    print(f"🎫 O seu código de entrada (QR Code) é: {nome_evento}")
                else:
                    print("Compra cancelada.")
            else:
                print("\033[91m❌ Desculpe, os bilhetes para este evento estão esgotados!\033[0m")
        else:
            print("❌ Evento não encontrado.")

    def validar_bilhete(self):
        print("\n--- 🎫 Validação de Bilhetes (Área Staff) ---")
        eventos = self.storage.carregar()

        codigo = input("Escaneie o QR Code ou digite o código do bilhete: ")

        nome_evento = codigo

        if nome_evento in eventos:
            evento = eventos[nome_evento]

            if evento["check_ins"] < evento["vendidos"]:
                eventos[nome_evento]["check_ins"] += 1
                self.storage.salvar(eventos)

                print("\033[92m✅ APROVADO: Bilhete validado com sucesso!\033[0m")
            else:
                print("\033[91m❌ ERRO: Bilhete já utilizado ou duplicado!\033[0m")
        else:
            print("❌ ERRO: Código/Evento inválido.")

    def exibir_dashboard(self):
        print("\n" + "=" * 40)
        print("📊 DASHBOARD DE VENDAS E OCUPAÇÃO")
        print("=" * 40)

        eventos = self.storage.carregar()

        if not eventos:
            print("Nenhum dado disponível.")
            return

        total_receita = 0
        total_bilhetes_vendidos = 0
        evento_mais_popular = None
        max_vendidos = -1

        for nome, info in eventos.items():
            vendidos = info["vendidos"]
            preco = info["preco"]
            total_bilhetes = info["total_bilhetes"]
            check_ins = info["check_ins"]

            receita_evento = vendidos * preco
            total_receita += receita_evento
            total_bilhetes_vendidos += vendidos

            lotacao = (
                vendidos / total_bilhetes * 100
                if total_bilhetes > 0
                else 0
            )

            ocupacao = (
                check_ins / vendidos * 100
                if vendidos > 0
                else 0
            )

            if vendidos > max_vendidos:
                max_vendidos = vendidos
                evento_mais_popular = nome

            print(f"\n📍 {nome}:")
            print(f"   - Receita: {receita_evento:.2f}€")
            print(f"   - Lotação: {lotacao:.1f}% ({vendidos} de {total_bilhetes})")
            print(f"   - Check-ins: {check_ins} de {vendidos} ({ocupacao:.1f}%)")

        print("\n" + "=" * 40)
        print(f"💰 RECEITA TOTAL: {total_receita:.2f}€")
        print(f"🎟️ TOTAL DE BILHETES: {total_bilhetes_vendidos}")
        print(f"🌟 EVENTO MAIS POPULAR: {evento_mais_popular}")
        print("=" * 40)