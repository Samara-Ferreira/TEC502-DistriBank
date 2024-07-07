'''
Descrição: este código contém a classe AccountManagement, que é responsável por gerenciar a conta do usuário no sistema
bancário.
'''

# Importar a biblioteca necessária
import requests
from os import system, name


# Classe que gerencia a conta do usuário no sistema bancário
class AccountManagement:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.cpf = None
        self.type = None

    # Método que limpa a tela
    def clear(self):
        # no windows e no linux
        system('cls' if name == 'nt' else 'clear')

    # Método que faz requisição para criar uma chave PIX
    def create_pix_key(self):
        print("\t", "-" * 60)
        print("\t\tCriação de uma chave PIX")
        print("\t", "-" * 60)

        print("\n\t| Digite o tipo de chave que deseja criar:")
        print("\t[1] CPF \t[2] E-mail \t[3] Telefone \t[4] Chave aleatória")

        option = 0
        while option < 1 or option > 4:
            try:
                option = int(input("\t> "))
            except ValueError:
                print("\n\t| Opção inválida! Digite um número inteiro.")
            except IndexError:
                print("\n\t| Opção inválida! Digite um número entre 1 e 4.")
            except KeyboardInterrupt:
                print("\n\t| Saindo...")
                exit(0)

        if option == 1:
            type_key = "cpf_cnpj"
        elif option == 2:
            type_key = "email"
        elif option == 3:
            type_key = "phone"
        elif option == 4:
            type_key = "random"

        print("\n\t Digite o valor da chave:")
        value = str(input("\t> "))

        try:
            response = requests.post(f"http://{self.host}:{self.port}/{self.cpf}/{self.type}/{type_key}/{value}"
                                    f"/create_pix_key")
            if response.status_code == 200:
                print(f"\n\t| {response.json()}")
            else:
                print(f"\n\t| {response.status_code}, {response.json()}")
        except requests.exceptions.ConnectionError:
            print("\n\t| Erro de conexão! Verifique se o servidor está ativo.")

    # Método que faz requisição para obter as chaves PIX
    def get_keys(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{self.type}/get_keys")
            if response.status_code == 200:
                print(f"\n\t\t\t| Chaves PIX do usuário {self.cpf}, {self.type} |")
                print(f"\t| {response.json()}")
            else:
                print(f"\n\t| {response.status_code}, {response.json()}")
        except requests.exceptions.ConnectionError:
            print("\n\t| Erro de conexão! Verifique se o servidor está ativo.")

    # Método que faz requisição para obter o saldo atual
    def get_balance(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{self.type}/get_balance")
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code, response.json()
        except requests.exceptions.ConnectionError:
            return "Erro de conexão! Verifique se o servidor está ativo."

    # Método que faz requisição para obter o extrato banco (completo)
    def get_statment(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/get_bank_statement")
            if response.status_code == 200:
                print(f"\n\t\t\t| Fila de execução |")
                print(f"\t{response.json()}")
            else:
                print(f"\n\t| {response.status_code}, {response.json()}")
        except requests.exceptions.ConnectionError:
            print("\n\t| Erro de conexão! Verifique se o servidor está ativo.")
