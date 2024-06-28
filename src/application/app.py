
import __init__
import requests
from os import system, name
from time import sleep

# import consortium.UniqueTwoDigitID as UniqueTwoDigitID


class Application():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.cpf = None
        self.user = None
        self.type_account = None
        self.queue_transfer = []
        # self.unique_id = UniqueTwoDigitID.UniqueTwoDigitID()

    # Método que faz a requisição de login
    def login(self):
        print("\n\t- Login [exemplo] -")
        option = input("\tDeseja fazer login com uma conta já existente? [1/2]: ")
        if option == "1":
            user = "thi03"
            password = "thiago123"
        else:
            user = "sil11"
            password = "silvio123"

        # print("\n\tDigite o seu usuário:")
        # user = input("\t> ")
        # print("\n\tDigite a sua senha:")
        # password = input("\t> ")

        response = requests.get(f"http://{self.host}:{self.port}/{user}/{password}/login")
        if response.status_code == 200:
            # Adicionar os dados principais na classe, para ficarem mais fáceis de serem obtidos
            self.user = user
            name, self.cpf, self.type_account = response.json().split(";")
            print(f"\n\t| Login realizado com sucesso para {name}, {self.type_account} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de logout
    def logout(self):
        response = requests.get(f"http://{self.host}:{self.port}/{self.user}/logout")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de criação de conta física
    def create_account_physics(self):
        print("\n\t- Criação de conta física [exemplo pronto] -")
        option = input("\tDeseja criar uma conta particular ou conjunta? [1/2]: ")
        if option == "1":
            name = "Thiago"
            cpf = "08300000000"
            user = "thi03"
            password = "thiago123"
            balance = 200.0
        else:
            name = "Silvio"
            cpf = "08500000000"
            user = "sil11"
            password = "silvio123"
            balance = 250.0
        # print("\tDigite o seu nome:")
        # name = str(input("\t> "))
        # print("\tDigite o seu CPF:")
        # cpf = str(input("\t> "))
        # print("\tDigite o seu usuário:")
        # user = str(input("\t> "))
        # print("\tDigite a sua senha:")
        # password = str(input("\t> "))
        # print("\tDigite o saldo inicial [mínimo R$ 100,00]:")
        # balance = float(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{name}/{cpf}/{user}/{password}/{balance}"
                                f"/create_physical_particular")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de criação de conta conjunta [admin]
    def create_account_joint(self):
        print("\n\t- Criação de conta conjunta [admin] [exemplo pronto] -")
        print("\tDigite o seu nome:")
        name = str(input("\t> "))
        print("\tDigite o seu CPF:")
        cpf = str(input("\t> "))
        print("\tDigite o seu usuário:")
        user = str(input("\t> "))
        print("\tDigite a sua senha:")
        password = str(input("\t> "))
        print("\tDigite o saldo inicial [mínimo R$ 100,00]:")
        balance = float(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{name}/{cpf}/{user}/{password}/{balance}"
                                f"/create_physical_joint")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de criação de conta conjunta [complementar]
    def create_account_complementary(self):
        print("\n\t- Criação de conta conjunta [complementar] [exemplo pronto] -")
        print("\tDigite o CPF do administrador:")
        cpf_holder = str(input("\t> "))
        print("\tDigite o seu nome:")
        name = input("\t> ")
        print("\tDigite o seu CPF:")
        cpf = input("\t> ")
        print("\tDigite o seu usuário:")
        user = input("\t> ")
        print("\tDigite a sua senha:")
        password = input("\t> ")

        response = requests.get(f"http://{self.host}:{self.port}/{cpf_holder}/{name}/{cpf}/{user}/{password}"
                                f"/create_joint_complementary")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de criação de conta jurídica [admin]
    def create_account_juridic(self):
        print("\n\t- Criação de conta jurídica [admin] [exemplo pronto] -")
        print("\tDigite o nome da empresa:")
        name = str(input("\t> "))
        print("\tDigite o CNPJ:")
        cnpj = str(input("\t> "))
        print("\tDigite o seu nome:")
        name_person = str(input("\t> "))
        print("\tDigite o seu usuário:")
        user = str(input("\t> "))
        print("\tDigite o seu CPF:")
        cpf = str(input("\t> "))
        print("\tDigite a sua senha:")
        password = input("\t> ")
        print("\tDigite o saldo inicial [mínimo R$ 300,00]:")
        balance = float(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{name}/{cnpj}/{name_person}/{user}/{cpf}/{password}/{balance}"
                                f"/create_juridic_account")
        if response.status_code == 200:
            #response = response.encode('utf-8').decode('unicode-escape')
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz a requisição de criação de conta jurídica [funcionário]
    def create_account_employee(self):
        print("\n\t- Criação de conta jurídica [funcionário] [exemplo pronto] -")
        print("\tDigite o CNPJ da empresa:")
        cnpj = str(input("\t> "))
        print("\n\tDigite o seu nome:")
        name = str(input("\t> "))
        print("\n\tDigite o seu usuário:")
        user = str(input("\t> "))
        print("\n\tDigite o seu CPF:")
        cpf = str(input("\t> "))
        print("\n\tDigite a sua senha:")
        password = str(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{cnpj}/{name}/{user}/{cpf}/{password}/"
                                f"create_juridic_employee")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz requisição para obter todas as contas do banco
    def get_all_accounts(self):
        response = requests.get(f"http://{self.host}:{self.port}/get_accounts")
        if response.status_code == 200:
            print("\t\t| Contas do banco |")
            print(f"\t{response.json()}")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz requisição para criar uma chave PIX
    def create_pix_key(self):
        print("\n\t- Criação de uma chave PIX -")
        option = input("\tDeseja criar uma chave PIX? [1/2]: ")

        if option == "1":
            type_key = "email"
            value = "thi@uefs"
        else:
            type_key = "email"
            value = "sil@uefs"

        # print("\tDigite o tipo de chave que deseja criar:")
        # print("\t1 - CPF")
        # print("\t2 - E-mail")
        # print("\t3 - Telefone")
        # print("\t4 - Chave aleatória")
        # type_key = str(input("\t> "))
        # type_key = "2"
        # if type_key == "1":
        #     type_key = "cpf-cnpj"
        # elif type_key == "2":
        #     type_key = "email"
        # elif type_key == "3":
        #     type_key = "phone"
        # elif type_key == "4":
        #     type_key = "random"
        #
        # print("\tDigite o valor da chave:")
        # value = str(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{self.type_account}/{type_key}/{value}"
                                f"/create_pix_key")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
            return response
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")
            return response

    # Método que faz requisição para obter as chaves PIX
    def get_keys(self):
        response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/get_keys")
        if response.status_code == 200:
            print("\t\t| Chaves PIX |")
            print(f"\t{response.json()}")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

    # Método que faz requisição para fazer um depósito
    def create_deposit(self):
        print("\n\t- Criação de um Depósito -")
        option = input("\tDeseja fazer um depósito? [1/2]: ")
        if option == "1":
            key = "thi@uefs"
            value = 50.0
        else:
            key = "sil@uefs"
            value = 50.0

        # print("\tDigite a chave PIX do destinatário:")
        # key = input("\t> ")
        # print("\tDigite o valor do depósito:")
        # value = float(input("\t> "))
        # id = self.port[-2:] + self.unique_id.generate()

        response = requests.get(f"http://{self.host}:{self.port}/{self.port}/{self.cpf}/{self.type_account}"
                                f"/{key}/{value}/create_deposit")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

    # Método que faz requisição para obter o saldo atual
    def get_balance(self):
        response = requests.get(f"http://{self.host}:{self.port}/{self.cpf}/{self.type_account}/get_balance")
        if response.status_code == 200:
            print(f"\t\t| Saldo da conta {self.cpf}, {self.type_account}|")
            print(f"\n\t| {response.json()} |")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

    # Método que faz requisição para obter o extrato banco (completo)
    def get_statment_bank(self):
        response = requests.get(f"http://{self.host}:{self.port}/get_queue_executed")
        if response.status_code == 200:
            print(f"\t\t| Fila de execução |")
            print(f"\n\t| {response.json()} |")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

    # Método que faz requisição para fazer um saque
    def create_withdraw(self):
        print("\n\t- Criação de um Saque -")
        option = input("\tDeseja fazer um saque? [1/2]: ")
        if option == "1":
            key = "thi@uefs"
            value = 50.0
        else:
            key = "sil@uefs"
            value = 50.0
        # print("\tDigite a chave PIX do destinatário:")
        # key = input("\t> ")
        # print("\tDigite o valor do saque:")
        # value = float(input("\t> "))

        response = requests.get(f"http://{self.host}:{self.port}/{self.port}/{self.cpf}/{self.type_account}"
                                f"/{key}/{value}/create_withdraw")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

    # Método que faz requisição para fazer uma transferência (pode ser apenas uma ou um pacote de transferências)
    def create_transfer(self):
        print("\n\t- Criação de uma Transferência -")
        # print("\tDigite a porta do banco destinatário:")
        # port_recp = intinput("\t> "))
        port_recp = 5551
        # print("\tDigite o CPF do destinatário:")
        # cpf_recp = str(input("\t> "))
        cpf_recp = "08300000000"
        # print("\tDigite o tipo de conta do destinatário:")
        # type_recp = str(input("\t> "))
        type_recp = "physical"
        # print("\tDigite a chave PIX do remetente:")
        # key_send = str(input("\t> "))
        key_send = "sil@uefs"
        # print("\tDigite a chave PIX do destinatário:")
        # key_recp = str(input("\t> "))
        key_recp = "thi@uefs"
        # print("\tDigite o valor da transferência:")
        # value = float(input("\t> "))
        value = 50.0

        operation = {"recipient": port_recp, "sender": self.port, "cpf_recipient": cpf_recp, "cpf_sender": self.cpf,
                     "type_recipient": type_recp, "type_sender": self.type_account, "key_recp": key_recp,
                     "key_send": key_send, "value": value, "operation": "transfer"}
        self.queue_transfer.append(operation)

        # print("\tDeseja fazer mais alguma transferência?")
        # print("\t1 - Sim")
        # print("\t2 - Não")
        # option = str(input("\t> "))
        option = "2"

        while option == "1":
            print("\n\t- Criação de uma Transferência -")
            print("\tDigite a porta do banco destinatário:")
            port_recp = str(input("\t> "))
            print("\tDigite o CPF do destinatário:")
            cpf_recp = str(input("\t> "))
            print("\tDigite o tipo de conta do destinatário:")
            type_recp = str(input("\t> "))
            print("\tDigite a chave PIX do destinatário:")
            key = input("\t> ")
            print("\tDigite o valor da transferência:")
            value = float(input("\t> "))
            operation = {"recipient": self.port, "sender": port_recp, "cpf_recipient": self.cpf, "cpf_sender": cpf_recp,
                         "type_recipient": self.type_account, "type_sender": type_recp, "key": key, "value": value,
                         "operation": "transfer"}
            self.queue_transfer.append(operation)

            print("\tDeseja fazer mais alguma transferência?")
            print("\t1 - Sim")
            print("\t2 - Não")
            option = str(input("\t> "))

        response = requests.post(f"http://{self.host}:{self.port}/{self.queue_transfer}/create_transfer")
        if response.status_code == 200:
            print(f"\n\t| {response.json()} |")
        else:
            print(f"\n\t| {response.status_code}, {response.json()} |")

        # limpar a lista
        self.queue_transfer = []
