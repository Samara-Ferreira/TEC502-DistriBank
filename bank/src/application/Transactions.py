'''
Descrição: este código contém a classe Transactions, responsável por gerenciar as transações do usuário no sistema
bancário.
'''

# Importar a biblioteca necessária
import ast
import requests
from os import system, name


# Classe que gerencia as transações do usuário no sistema bancário
class Transactions:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.cpf = None
        self.type = None
        self.pix_key = None
        self.queue_transfer = []
        # self.banks = [
        #         {"host": "172.16.103.1", "port": 5551, "active": False},
        #         {"host": "172.16.103.2", "port": 5552, "active": False},
        #         {"host": "172.16.103.4", "port": 5553, "active": False},
        #         {"host": "172.16.103.5", "port": 5554, "active": False}
        # ]
        self.banks = [
                {"host": "172.22.208.1", "port": 5551, "active": False},
                {"host": "172.22.208.1", "port": 5552, "active": False},
                {"host": "172.22.208.1", "port": 5553, "active": False},
                {"host": "172.22.208.1", "port": 5554, "active": False}
        ]

    # Método para limpar a tela
    def clear(self):
        # no windows e no linux
        system('cls' if name == 'nt' else 'clear')

    # Método que faz requisição para fazer um depósito
    def create_deposit(self):
        print("\t", "-" * 60)
        print("\t\t\tCriação de um depósito")
        print("\t", "-" * 60)

        print("\n\t Digite o valor do depósito:")
        value = float(input("\t> "))

        response = requests.post(f"http://{self.host}:{self.port}/{self.host}/{self.port}/{self.cpf}/{self.type}/{value}"
                                 f"/create_deposit")

        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Método que faz requisição para fazer um saque
    def create_withdraw(self):
        print("\t", "-" * 60)
        print("\t\t\tCriação de um saque")
        print("\t", "-" * 60)

        print("\n\t Digite o valor do saque:")
        value = float(input("\t> "))

        actual_balance = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{self.type}/get_balance")
        if actual_balance.status_code == 200:
            actual_balance = actual_balance.json()
            if value > actual_balance:
                print("\n\t| Saldo insuficiente! Tente novamente.")
                return None

            response = requests.post(f"http://{self.host}:{self.port}/{self.host}/{self.port}/{self.cpf}/{self.type}/{value}"
                                     f"/create_withdraw")

            if response.status_code == 200:
                print(f"\n\t| {response.json()}")
            else:
                print(f"\n\t| {response.status_code}, {response.json()}")
        else:
            print(f"\n\t| {actual_balance.status_code}, {actual_balance.json()}")

    # Método que faz requisição para fazer uma transferência (pode ser apenas uma ou um pacote de transferências)
    def create_transfer(self):
        print("\t", "-" * 60)
        print("\t\t\tCriação de uma transferência")
        print("\t", "-" * 60)

        operation = self.create_one_transfer()

        while operation is None:
            operation = self.create_one_transfer()

        self.queue_transfer.append(operation)

        option = self.more_transactions()

        while option == 1:
            self.clear()
            operation = self.create_one_transfer()
            self.queue_transfer.append(operation)
            option = self.more_transactions()

        response = requests.post(f"http://{self.host}:{self.port}/{self.queue_transfer}/create_transfer")
        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

        # limpar a lista
        self.queue_transfer = []

    # Método para criar apenas uma transferência
    def create_one_transfer(self):
        print("\n\t| De qual banco você deseja transferir?")
        for bank in self.banks:
            print(f"\tBanco {self.banks.index(bank) + 1}: Host: {bank['host']} - Porta: {bank['port']}")

        type_bank_send = 0
        while type_bank_send < 1 or type_bank_send > 4:
            try:
                type_bank_send = int(input("\t> "))
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 4.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)

        print("\n\t| Qual o tipo de conta que você deseja transferir?")
        print("\n\t[1] Conta física particular \n\t[2] Conta física conjunta \n\t[3] Conta jurídica")

        type_account_send = 0
        while type_account_send < 1 or type_account_send > 3:
            try:
                type_account_send = int(input("\t> "))
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 3.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)

        if type_account_send == 1:
            type_account_send = "physical"
        elif type_account_send == 2:
            type_account_send = "physical_joint"
        else:
            type_account_send = "juridic"

        host_send = self.banks[type_bank_send - 1]["host"]
        port_send = self.banks[type_bank_send - 1]["port"]

        # Verifica se o cliente existe naquele banco VERIFICAR SE O BANCO ESTÁ ATIVO
        try:
            response = requests.get(f"http://{host_send}:{port_send}/{self.cpf}/{type_account_send}/check_client")
        except requests.exceptions.ConnectionError:
            self.clear()
            print("\n\t| Banco indisponível! Tente novamente mais tarde.")
            return None

        if response.status_code == 200:
            print("\n\t", "-" * 60)

            print("\n\t Digite a chave PIX do destinatário:")
            key_recp = str(input("\t> "))

            check_key = None
            # Verificar se a chave pix existe em algum dos bancos
            try:
                for bank in self.banks:
                    response = requests.get(f"http://{bank['host']}:{bank['port']}/{key_recp}/check_key"
                                            f"")
                    if response.status_code == 200:
                        check_key = "OK"
                        host_recp = bank['host']
                        port_recp = bank['port']
                        # Transforma em lista novamente
                        response = ast.literal_eval(response.json())
                        cpf_recp = response[0]
                        type_recp = response[1]
                        break
            except requests.exceptions.ConnectionError:
                self.clear()
                print("\n\t| Banco indisponível! Tente novamente mais tarde.")
                return None

            if check_key is None:
                self.clear()
                print("\n\t| Chave PIX inválida! Tente novamente.")
                return None

            print("\n\t Digite o valor da transferência:")
            value = float(input("\t> "))
            while value < 0:
                print("\n\t| Valor inválido! Digite um valor positivo.")
                value = float(input("\t> "))

            # # Verificar se tem saldo suficiente
            # try:
            #     response = requests.get(f"http://{host_send}:{port_send}/{self.cpf}/{type_account_send}/get_balance")
            # except requests.exceptions.ConnectionError:
            #     self.clear()
            #     print("\n\t| Banco indisponível! Tente novamente mais tarde.")
            #     return None
            #
            # if response.status_code != 200:
            #     self.clear()
            #     print(f"\n\t| {response.status_code}, {response.json()}")
            #     return None
            #
            # actual_balance = response.json()
            # if value > actual_balance:
            #     self.clear()
            #     print("\n\t| Saldo insuficiente! Tente novamente.")
            #     return None

            operation = {"host_recp": host_recp, "port_recp": port_recp, "cpf_recp": cpf_recp,
                         "type_recp": type_recp, "key_recp": key_recp,
                         "host_send": host_send, "port_send": port_send, "cpf_send": self.cpf,
                         "type_send": type_account_send, "value": value, "operation": "transfer"}
            return operation

        else:
            self.clear()
            print(f"\n\t| {response.status_code}, {response.json()}")
            return None

    # Método que verifica se o usuário quer realizar mais uma transação
    def more_transactions(self):
        option = 0
        while option < 1 or option > 2:
            try:
                print("\n\t| Deseja fazer mais alguma transferência?")
                print("\t\t[1] Sim \t[2] Não")
                option = int(input("\t> "))
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 2.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)
        return option

    # Aceitar somente números e 11 dígitos
    def check_cpf(self, cpf):
        while not cpf.isdigit() or len(cpf) != 11:
            print("\n\t| CPF inválido! Digite apenas números e 11 dígitos.")
            cpf = str(input("\t> "))
        return cpf
