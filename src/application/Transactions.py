'''
Descrição: este código contém a classe Transactions, que é responsável por gerenciar as transações do usuário no sistema
bancário.
'''

# Importar a biblioteca necessária
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
        self.banks = [
                {"host": "192.168.0.111", "port": 5551, "active": False},
                {"host": "192.168.0.111", "port": 5552, "active": False},
                {"host": "192.168.0.111", "port": 5553, "active": False},
                {"host": "192.168.0.111", "port": 5554, "active": False}
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

        response = requests.get(f"http://{self.host}:{self.port}/{self.host}/{self.port}/{self.cpf}/{self.type}/{value}"
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

        response = requests.get(f"http://{self.host}:{self.port}/{self.host}/{self.port}/{self.cpf}/{self.type}/{value}"
                                 f"/create_withdraw")

        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Método que faz requisição para fazer uma transferência (pode ser apenas uma ou um pacote de transferências)
    def create_transfer(self):
        print("\t", "-" * 60)
        print("\t\t\tCriação de uma transferência")
        print("\t", "-" * 60)

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
        # IDEIA: AO INVES DE PEDIR A PORTA, PROCURAR PELO CPF DO CLIENTE
        print("\n\t| De qual banco você deseja transferir?")
        for bank in self.banks:
            print(f"\tBanco {self.banks.index(bank) + 1}: Host: {bank['host']} - Porta: {bank['port']}")
        type_bank = int(input("\t> "))

        while type_bank < 1 or type_bank > 4:
            print("\n\t| Opção inválida! Digite um número entre 1 e 4.")
            type_bank = int(input("\t> "))

        print("\n\t E qual o tipo de conta?")
        type_account = str(input("\t> ")).lower()

        # Verifica se o cliente existe naquele banco
        response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{type_account}/check_client")
        if response.status_code == 200:
            host_send = self.banks[type_bank - 1]["host"]
            port_send = self.banks[type_bank - 1]["port"]

            print("\n\t E para qual banco você deseja transferir?")
            for bank in self.banks:
                print(f"\tBanco {self.banks.index(bank) + 1}: Host: {bank['host']} - Porta: {bank['port']}")
            type_bank = int(input("\t> "))

            while type_bank < 1 or type_bank > 4:
                print("\n\t| Opção inválida! Digite um número entre 1 e 4.")
                type_bank = int(input("\t> "))
            host_recp = self.banks[type_bank - 1]["host"]
            port_recp = self.banks[type_bank - 1]["port"]

            print("\n\t Digite o CPF do destinatário:")
            cpf_recp = str(input("\t> "))
            print("\n\t Digite o tipo de conta do destinatário:")
            type_recp = str(input("\t> "))
            # print("\n\t Digite a chave PIX do remetente:")
            # key_send = str(input("\t> "))
            print("\n\t Digite a chave PIX do destinatário:")
            key_recp = str(input("\t> "))
            print("\n\t Digite o valor da transferência:")
            value = float(input("\t> "))

            operation = {"host_recp": host_recp, "port_recp": port_recp, "cpf_recp": cpf_recp, "type_recp": type_recp,
                         "key_recp": key_recp,
                         "host_send": host_send, "port_send": port_send, "cpf_send": self.cpf, "type_send": type_account,
                         "value": value, "operation": "transfer"}
            return operation

        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

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
