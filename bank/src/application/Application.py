'''
Descrição: este código contém a classe Application, que é responsável por gerenciar a aplicação do sistema bancário.
'''

# Importar as bibliotecas necessárias
import __init__
import ast
import requests

from os import system, name
from Transactions import Transactions
from AccountCreation import CreateAccount
from AccountManagement import AccountManagement


# Classe que gerencia a aplicação do sistema bancário
class Application:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.cpf = None
        self.name = None
        self.user = None
        self.type = None
        self.queue_transfer = []
        self.create_account = CreateAccount(host, port)
        self.account_management = AccountManagement(host, port)
        self.transactions = Transactions(host, port)

    # Método para limpar a tela
    def clear(self):
        # no windows e no linux
        system('cls' if name == 'nt' else 'clear')

    # Método que faz a requisição de login
    def login(self):
        self.clear()
        print("\t", "-"*60)
        print("\t\t\tLogin no sistema bancário")
        print("\t", "-"*60)

        print("\n\t| Qual o tipo de conta?")
        print("\n\t[1] Conta física particular \n\t[2] Conta física conjunta \n\t[3] Conta jurídica")
        type_account = 0
        while type_account < 1 or type_account > 3:
            try:
                type_account = int(input("\t> "))
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 3.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)
        if type_account == 1:
            type_account = "physical"
        elif type_account == 2:
            type_account = "physical_joint"
        else:
            type_account = "juridic"


        print("\n\t Digite o seu usuário:")
        user = str(input("\t> "))

        print("\n\t Digite a sua senha:")
        password = str(input("\t> "))

        response = requests.post(f"http://{self.host}:{self.port}/{type_account}/{user}/{password}/login")
        if response.status_code == 200:
            self.user = user
            self.name, self.cpf, self.type = response.json().split(";")

            self.account_management.cpf = self.cpf
            self.account_management.type = self.type
            self.transactions.cpf = self.cpf
            self.transactions.type = self.type

            print(f"\n\t| Login realizado com sucesso para {self.name}\n")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()}\n")
            return response

    # Método que faz a requisição de logout
    def logout(self):
        response = requests.post(f"http://{self.host}:{self.port}/{self.user}/logout")
        if response.status_code == 200:
            print(f"\n\t| {response.json()}\n")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}\n")

    # Método que faz requisição para obter a lista de clients
    def get_clients(self):
        response = requests.get(f"http://{self.host}:{self.port}/get_clients")
        if response.status_code == 200:
            self.clear()
            # Transformar a string em lista
            list_clients = ast.literal_eval(response.json())
            print("\t", "-"*60)
            print("\t\t\tLista de clientes do banco")
            print("\t", "-"*60)

            for client in list_clients:
                print(f"\t| {client}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}\n")
