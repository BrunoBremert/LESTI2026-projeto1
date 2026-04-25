from storage.json_storage import JsonStorage
from services.usuario_service import UsuarioService
from services.evento_service import EventoService
from services.bilhete_service import BilheteService


class SistemaBilheteria:
    def __init__(self):
        usuario_storage = JsonStorage("data/usuarios.json")
        evento_storage = JsonStorage("data/eventos.json")

        self.usuario_service = UsuarioService(usuario_storage)
        self.evento_service = EventoService(evento_storage)
        self.bilhete_service = BilheteService(evento_storage, self.evento_service)

    def pedir_opcao(self):
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
            return None

    def mostrar_menu(self):
        print("\n" + "=" * 30)
        print("🎫 SISTEMA DE BILHETERIA")
        print("=" * 30)
        print("1. Registrar Utilizador")
        print("2. Login")
        print("3. Cadastrar Evento (Organizador/Create)")
        print("4. Listar Eventos (Read)")
        print("5. Editar Evento (Organizador/Update)")
        print("6. Excluir Evento (Organizador/Delete)")
        print("7. Comprar Bilhete (Cliente)")
        print("8. Validar Bilhete (Staff/Check-in)")
        print("9. Dashboard")
        print("10. Sair")

    def executar(self):
        while True:
            self.mostrar_menu()

            opcao = self.pedir_opcao()

            if opcao is None:
                continue

            if opcao == 1:
                self.usuario_service.registrar_usuario()
            elif opcao == 2:
                self.usuario_service.fazer_login()
            elif opcao == 3:
                self.evento_service.cadastrar_evento()
            elif opcao == 4:
                self.evento_service.listar_eventos()
            elif opcao == 5:
                self.evento_service.editar_evento()
            elif opcao == 6:
                self.evento_service.excluir_evento()
            elif opcao == 7:
                self.bilhete_service.comprar_bilhete()
            elif opcao == 8:
                self.bilhete_service.validar_bilhete()
            elif opcao == 9:
                self.bilhete_service.exibir_dashboard()
            elif opcao == 10:
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    sistema = SistemaBilheteria()
    sistema.executar()