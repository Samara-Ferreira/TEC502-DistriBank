'''
Descrição: este código é o principal da aplicação do sistema bancário e contém as funções de menu.
'''

# Importar as bibliotecas necessárias
from time import sleep
from os import system, name
from Application import Application

banks = [
    {"host": "192.168.0.111", "port": 5551, "active": False},
    {"host": "192.168.0.111", "port": 5552, "active": False},
    {"host": "192.168.0.111", "port": 5553, "active": False},
    {"host": "192.168.0.111", "port": 5554, "active": False}
]


# Limpar o terminal antes de iniciar
def clear():
    # no windows e no linux
    system('cls' if name == 'nt' else 'clear')


# Menu do banco financeiro
def menu_bank():
    operation = 10
    while operation != 0:
        clear()
        print("\t", "-"*60)
        print(f"\t\tMenu do banco financeiro {banks[bank - 1]['host']}:{banks[bank - 1]['port']}")
        print("\t", "-"*60)

        print("\t| Bem-vindo(a), ", app.name, "!")
        print("\t| CPF: ", app.cpf)
        print("\t| Tipo de conta: ", app.type)
        print("\t| Saldo atual: R$", app.account_management.get_balance(), "\n")


        print("\t", "-"*60)
        print("\t\t\tOperações dispníveis")
        print("\t", "-"*60)

        print("\t[1] Criar uma chave pix")
        print("\t[2] Visualizar minhas chaves pix")
        print("\t[3] Depositar na conta")
        print("\t[4] Sacar da conta")
        print("\t[5] Transferir para outra conta")
        #print("\t[6] Extrato da conta")
        print("\t[0] Sair\n")

        print("\n\t Digite o número correspondente à operação desejada:")
        operation = int(input("\t> "))

        if operation == 0:
            print("\n\t| Saindo...")
            sleep(1)
            app.logout()

        elif operation == 1:
            clear()
            app.account_management.create_pix_key()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 2:
            clear()
            app.account_management.get_keys()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 3:
            clear()
            app.transactions.create_deposit()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 4:
            clear()
            app.transactions.create_withdraw()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 5:
            clear()
            app.transactions.create_transfer()
            input("\n\tPressione qualquer tecla para continuar...")

            '''elif operation == 6:
                clear()
                app.account_management.get_statment()
                input("\n\tPressione qualquer tecla para continuar...")'''

        else:
            print("\n\t| Operação inválida!")


# Menu inicial do sistema bancário
def initial_menu():
    while banks[bank - 1]["active"]:
        clear()

        print("\t", "-"*60)
        print("\t\t\tMenu inicial do sistema bancário")
        print("\t", "-"*60)

        print("\t[1] Login em uma conta existente")
        print("\t[2] Criar uma nova conta")
        print("\t[3] Visualiar todos os clientes")
        print("\t[4] Visualizar histórico de transações")
        print("\t[0] Desativar esse banco")

        print("\n\t Digite o número correspondente à operação desejada:")
        operation = int(input("\t> "))

        if operation == 0:
            banks[bank - 1]["active"] = False
            exit(0)

        elif operation == 1:
            response = app.login()
            if response.status_code == 200:
                print("\t| Tentativa de login na conta...")
                sleep(1)
                menu_bank()

        elif operation == 2:
            print("\t", "-"*60)
            print("\n\t| Qual tipo de conta deseja criar?\n")
            print("\t[1] Conta física particular")
            print("\t[2] Conta conjunta (titular)")
            print("\t[3] Conta conjunta (complementar)")
            print("\t[4] Conta jurídica (admin)")
            print("\t[5] Conta jurídica (funcionário)")

            type = 0
            while type <= 0 or type > 5:
                try:
                    type = int(input("\t> "))
                except ValueError:
                    print("\n\t Tipo de conta inválido!")
                except IndexError:
                    print("\n\t Opção inválida! Digite um número entre 1 e 5.")
                except KeyboardInterrupt:
                    print("\n\tSaindo...")
                    exit(0)

            if type == 1:
                app.create_account.create_account_physics()
            elif type == 2:
                app.create_account.create_account_joint()
            elif type == 3:
                app.create_account.create_account_complementary()
            elif type == 4:
                app.create_account.create_account_juridic()
            elif type == 5:
                app.create_account.create_account_employee()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 3:
            clear()
            app.get_clients()
            input("\n\tPressione qualquer tecla para continuar...")

        elif operation == 4:
            clear()
            app.account_management.get_statment()
            input("\n\tPressione qualquer tecla para continuar...")

        else:
            print("\n\t| Operação inválida!")


# Iniciar a aplicação
if __name__ == "__main__":
    clear()

    try:
        print("\t", "-"*60)
        print("\t\t\tBem-vindo ao banco financeiro!")
        print("\t", "-"*60)

        print("\n\t| Com qual banco deseja se conectar?\n")
        for bank in banks:
            print(f"\tBanco {banks.index(bank) + 1}: Host: {bank['host']} - Porta: {bank['port']}")
        print("\n\t[0] Sair\n")

        # Escolher um banco; caso seja uma opção inválida, pede para que o usuário insera novamente
        bank = 0
        while bank <= 0 or bank > 4:
            try:
                print("\n\t Digite o número correspondente ao banco desejado:")
                bank = int(input("\t> "))
                banks[bank - 1]["active"] = True
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 4.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)

        # Conectar ao banco escolhido
        if bank == 1:
            app = Application(banks[0]["host"], banks[0]["port"])
            app.host = banks[0]["host"]
            app.port = str(banks[0]["port"])
        elif bank == 2:
            app = Application(banks[1]["host"], banks[1]["port"])
            app.host = banks[1]["host"]
            app.port = str(banks[1]["port"])
        elif bank == 3:
            app = Application(banks[2]["host"], banks[2]["port"])
            app.host = banks[2]["host"]
            app.port = str(banks[2]["port"])
        elif bank == 4:
            app = Application(banks[3]["host"], banks[3]["port"])
            app.host = banks[3]["host"]
            app.port = str(banks[3]["port"])
        elif bank == 0:
            print("\n\t| Saindo...")
            exit(0)

        initial_menu()

    except KeyboardInterrupt:
        print("\n\t| API encerrada!")
        sleep(0.5)
        exit(0)

