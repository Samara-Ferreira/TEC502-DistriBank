


# Importar as bibliotecas necessárias
import __init__
from os import system, name
from app import Application
from time import sleep


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


def menu_bank():
    operation = 10
    while operation != 1:
        clear()
        print(f"\n\t- Menu do banco financeiro {banks[bank - 1]['host']}:{banks[bank - 1]['port']} -\n")
        print("\t\t", app.get_balance(), "\n")

        print("\t1 - Deslogar") # feito
        print("\t2 - Criação chave pix")    # feito
        print("\t3 - Listar chaves pix")    # feito
        print("\t4 - Depositar")
        print("\t5 - Sacar")
        print("\t6 - Transferir")
        print("\t7 - Extrato [por enquanto, ta de tudo]")
        print("\t0 - Sair\n")

        print("\n\tDigite o número correspondente à operação desejada:")
        operation = int(input("\t> "))

        if operation == 1:
            clear()
            app.logout()

        elif operation == 2:
            clear()
            app.create_pix_key()

        elif operation == 3:
            clear()
            app.get_keys()

        elif operation == 4:
            clear()
            app.create_deposit()

        elif operation == 5:
            clear()
            app.create_withdraw()

        elif operation == 6:
            clear()
            app.create_transfer()

        elif operation == 7:
            clear()
            app.get_statment_bank()

        else:
            print("\n\tOperação inválida!")

        input("\n\tPressione qualquer tecla para continuar...")


def menu_initial():
    while banks[bank - 1]["active"]:
        clear()
        print("\n\t- Menu inicial -\n")
        print("\t1 - Login")
        print("\t2 - Criar conta")
        print("\t3 - Listar contas")
        print("\t4 - Obter o extrato bancário")
        print("\t0 - Desativar banco")

        print("\n\tDigite o número correspondente à operação desejada:")
        operation = int(input("\t> "))

        if operation == 1:
            response = app.login()
            if response.status_code == 200:
                sleep(1)
                menu_bank()

        elif operation == 2:
            clear()
            print("\n\tDigite o tipo de conta que deseja criar:")
            print("\t1 - Conta física")
            print("\t2 - Conta conjunta admin")
            print("\t3 - Conta conjunta complementar")
            print("\t4 - Conta jurídica admin")
            print("\t5 - Conta jurídica funcionário")

            type = int(input("\t> "))
            if type == 1:
                app.create_account_physics()
            elif type == 2:
                app.create_account_joint()
            elif type == 3:
                app.create_account_complementary()
            elif type == 4:
                app.create_account_juridic()
            elif type == 5:
                app.create_account_employee()
            else:
                print("\n\tTipo de conta inválido!")

        elif operation == 3:
            clear()
            app.get_all_accounts()

        elif operation == 4:
            clear()
            app.get_statment_bank()

        elif operation == 0:
            banks[bank - 1]["active"] = False
            exit(0)

        else:
            clear()
            print("\n\tOperação inválida!")

        input("\n\tPressione qualquer tecla para continuar...")


if __name__ == "__main__":
    clear()

    try:
        print("\tBem-vindo ao banco financeiro!\n")
        print("\n\tCom qual banco deseja se conectar?\n")
        for bank in banks:
            print(f"\tBanco: {banks.index(bank) + 1} - Host: {bank['host']} - Porta: {bank['port']}")
        print("\t0 - Sair\n")

        print("\n\tDigite o número correspondente ao banco desejado:")
        bank = int(input("\t> "))

        # Ativando o banco escolhido
        banks[bank - 1]["active"] = True

        if bank == 1:
            app = Application(banks[0]["host"], banks[0]["port"])
            app.host = banks[0]["host"]
            app.port = str(banks[0]["port"])
        elif bank == 2:
            app = Application(banks[1]["host"], banks[1]["port"])
            app.host = banks[0]["host"]
            app.port = str(banks[0]["port"])
        elif bank == 3:
            app = Application(banks[2]["host"], banks[2]["port"])
            app.host = banks[0]["host"]
            app.port = str(banks[0]["port"])
        elif bank == 4:
            app = Application(banks[3]["host"], banks[3]["port"])
            app.host = banks[0]["host"]
            app.port = str(banks[0]["port"])
        elif bank == 0:
            print("\n\tSaindo...")
            exit(0)

        menu_initial()

    except KeyboardInterrupt:
        print("Api encerrada!")
        sleep(0.5)
        exit(0)

