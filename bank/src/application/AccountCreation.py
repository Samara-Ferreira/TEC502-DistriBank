'''
Descrição: este código contém a classe CreateAccount, que é responsável por gerenciar a criação de contas no sistema
bancário.
'''

# Importar a biblioteca necessária
import requests
from os import system, name


# Classe que gerencia a criação de contas no sistema bancário
class CreateAccount:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # Método para limpar a tela
    def clear(self):
        # no windows e no linux
        system('cls' if name == 'nt' else 'clear')

    # Método que faz a requisição de criação de conta física
    def create_account_physics(self):
        self.clear()
        print("\t", "-" * 60)
        print("\t\tCriação de conta física particular")
        print("\t", "-" * 60)

        print("\n\t Digite o seu nome:")
        name = str(input("\t> ")).capitalize()
        name = self.check_name(name).capitalize()

        print("\n\t Digite o seu CPF:")
        cpf = str(input("\t> "))
        cpf = self.check_cpf(cpf)

        print("\n\t Digite o seu usuário:")
        user = str(input("\t> ")).lower()
        user = self.check_user(user).lower()

        print("\n\t Digite a sua senha:")
        password = str(input("\t> ")).lower()
        password = self.check_password(password).lower()

        print("\n\t Digite o saldo inicial [mínimo R$ 100,00]:")
        balance = float(input("\t> "))
        balance = self.check_balance(balance, 100.00)

        response = requests.post(f"http://{self.host}:{self.port}/{name}/{cpf}/{user}/{password}/{balance}"
                                f"/create_physical_particular")
        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")
            return response

    # Método que faz a requisição de criação de conta conjunta [admin]
    def create_account_joint(self):
        self.clear()
        print("\t", "-" * 60)
        print("\t\tCriação de conta conjunta [titular]")
        print("\t", "-" * 60)

        print("\n\t Digite o seu nome:")
        name = str(input("\t> ")).capitalize()
        name = self.check_name(name).capitalize()

        print("\n\t Digite o seu CPF:")
        cpf = str(input("\t> "))
        cpf = self.check_cpf(cpf)

        print("\n\t Digite o seu usuário:")
        user = str(input("\t> ")).lower()
        user = self.check_user(user).lower()

        print("\n\t Digite a sua senha:")
        password = str(input("\t> ")).lower()
        password = self.check_password(password).lower()

        print("\n\t Digite o saldo inicial [mínimo R$ 200,00]:")
        balance = float(input("\t> "))
        balance = self.check_balance(balance, 200.00)

        response = requests.post(f"http://{self.host}:{self.port}/{name}/{cpf}/{user}/{password}/{balance}"
                                f"/create_physical_joint")
        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Método que faz a requisição de criação de conta conjunta [complementar]
    def create_account_complementary(self):
        self.clear()
        print("\t", "-" * 60)
        print("\t\tCriação de conta conjunta [complementar]")
        print("\t", "-" * 60)

        print("\n\t Digite o CPF do administrador:")
        cpf_holder = str(input("\t> "))
        cpf_holder = self.check_cpf(cpf_holder)

        print("\n\t Digite o seu nome:")
        name = str(input("\t> ")).capitalize()
        name = self.check_name(name).capitalize()

        print("\n\t Digite o seu CPF:")
        cpf = str(input("\t> "))
        cpf = self.check_cpf(cpf)

        print("\n\t Digite o seu usuário:")
        user = str(input("\t> ")).lower()
        user = self.check_user(user).lower()

        print("\n\t Digite a sua senha:")
        password = str(input("\t> ")).lower()
        password = self.check_password(password).lower()

        response = requests.post(f"http://{self.host}:{self.port}/{cpf_holder}/{name}/{cpf}/{user}/{password}"
                                f"/create_joint_complementary")
        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Método que faz a requisição de criação de conta jurídica [admin]
    def create_account_juridic(self):
        self.clear()
        print("\t", "-" * 60)
        print("\t\tCriação de conta jurídica [titular]")
        print("\t", "-" * 60)

        print("\n\t Digite o nome da empresa:")
        name = str(input("\t> ")).capitalize()
        name = self.check_name(name).capitalize()

        print("\n\t Digite o CNPJ:")
        cnpj = str(input("\t> "))
        cnpj = self.check_cnpj(cnpj)

        print("\n\t Digite o seu nome:")
        name_person = str(input("\t> ")).capitalize()
        name_person = self.check_name(name_person).capitalize()

        print("\n\t Digite o seu usuário:")
        user = str(input("\t> ")).lower()
        user = self.check_user(user).lower()

        print("\n\t Digite o seu CPF:")
        cpf = str(input("\t> "))
        cpf = self.check_cpf(cpf)

        print("\n\t Digite a sua senha:")
        password = input("\t> ").lower()
        password = self.check_password(password).lower()

        print("\n\t Digite o saldo inicial [mínimo R$ 300,00]:")
        balance = float(input("\t> "))
        balance = self.check_balance(balance, 300.00)

        response = requests.post(f"http://{self.host}:{self.port}/{name}/{cnpj}/{name_person}/{user}/{cpf}/{password}"
                                f"/{balance}/create_juridic_account")

        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Método que faz a requisição de criação de conta jurídica [funcionário]
    def create_account_employee(self):
        self.clear()
        print("\t", "-" * 60)
        print("\t\tCriação de conta jurídica [funcionário]")
        print("\t", "-" * 60)

        print("\n\t Digite o CNPJ da empresa:")
        cnpj = str(input("\t> "))
        cnpj = self.check_cnpj(cnpj)

        print("\n\t Digite o seu nome:")
        name = str(input("\t> ")).capitalize()
        name = self.check_name(name).capitalize()

        print("\n\t Digite o seu usuário:")
        user = str(input("\t> ")).lower()
        user = self.check_user(user).lower()

        print("\n\t Digite o seu CPF:")
        cpf = str(input("\t> "))
        cpf = self.check_cpf(cpf)

        print("\n\t Digite a sua senha:")
        password = str(input("\t> ")).lower()
        password = self.check_password(password).lower()

        response = requests.post(f"http://{self.host}:{self.port}/{cnpj}/{name}/{user}/{cpf}/{password}"
                                f"/create_juridic_employee")

        if response.status_code == 200:
            print(f"\n\t| {response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()}")

    # Aceitar somente letras e espaços
    def check_name(self, name):
        while not name.replace(" ", "").isalpha():
            print("\n\t| Nome inválido! Digite apenas letras e espaços.")
            name = str(input("\t> "))
        return name

    # Aceitar somente números
    def check_phone(self, phone):
        while not phone.isdigit():
            print("\n\t| Telefone inválido! Digite apenas números.")
            phone = str(input("\t> "))
        return

    # Aceitar somente números e 11 dígitos
    def check_cpf(self, cpf):
        while not cpf.isdigit() or len(cpf) != 11:
            try:
                print("\n\t| CPF inválido! Digite apenas números e 11 dígitos.")
                cpf = str(input("\t> "))
            except ValueError:
                print("\n\t| CPF inválido! Digite apenas números e 11 dígitos.")
                cpf = str(input("\t> "))
        return cpf

    # Aceitar somente números e 14 dígitos
    def check_cnpj(self, cnpj):
        while not cnpj.isdigit() or len(cnpj) != 14:
            print("\n\t| CNPJ inválido! Digite apenas números e 14 dígitos.")
            cnpj = str(input("\t> "))
        return cnpj

    # Aceitar somente letras, números e sem espaços e com no máximo 6 caracteres
    def check_user(self, user):
        while not user.isalnum() or len(user) > 6:
            try:
                print("\n\t| Usuário inválido! Digite apenas letras e números, sem espaços e com no máximo 6 "
                      "caracteres.")
                user = str(input("\t> "))
            except ValueError:
                print("\n\t| Usuário inválido! Digite apenas letras e números, sem espaços e com no máximo 6 "
                      "caracteres.")
                user = str(input("\t> "))
        return user

    # Aceitar somente letras, números e sem espaços e com no máximo 6 caracteres
    def check_password(self, password):
        while not password.isalnum() or len(password) > 6:
            try:
                print("\n\t| Senha inválida! Digite apenas letras e números, sem espaços e com no máximo 6 caracteres.")
                password = str(input("\t> "))
            except ValueError:
                print("\n\t| Senha inválida! Digite até no máximo 6 caracteres, sem espaço.")
                password = str(input("\t> "))
        return password

    # Aceitar somente números e com valor mínimo de R$ 100,00
    def check_balance(self, balance, min_balance):
        while balance < min_balance:
            try:
                print(f"\n\t| Saldo inválido! Digite um valor numérico e com o mínimo de R$ {min_balance:.2f}.")
                balance = float(input("\t> "))
            except ValueError:
                print(f"\n\t| Saldo inválido! Digite um valor numérico e com o mínimo de R$ {min_balance:.2f}.")
                balance = float(input("\t> "))
        return balance
