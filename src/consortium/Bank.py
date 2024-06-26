'''
Descrição: Arquivo referente a classe consortium e seus métodos, onde são definidas as funções principais do banco,
como criar conta, deletar conta, criar chave pix, depositar e sacar dinheiro, realizar transações, entre outras.
'''

# Importar as bibliotecas necessárias
import __init__
import ast
import json
import requests
import utils.Utils as Utils
import exceptions.Exceptions as Exceptions
import clients.JuridicAccount as JuridicAccount
import clients.PhysicalAccount as PhysicalAccount

from threading import Lock
from Operations import Operations
from socket import gethostbyname, gethostname


class Bank:
    def __init__(self, name, port):
        self.cnpj = gethostbyname(gethostname())
        self.name = name
        self.port = port
        self.clients = {}
        self.operations = Operations(self.port, self.cnpj)
        self.lock = Lock()

    # Método para fazer login na conta

    # Método para deslogar da conta

    # ------------------------------------ Funções para a criação das contas ------------------------------------ #

    def create_physical_particular(self, name, cpf, user, password, balance):
        with self.lock:
            if cpf in self.clients:
                raise Exceptions.ClientAlreadyExists

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF
            elif balance < 100:
                raise Exceptions.InvalidBalance
            new_client = PhysicalAccount.PhysicalClient(name, cpf, user, password, balance, agency, account)
            self.clients[cpf] = new_client
            return f"Conta particular para {name} criada com sucesso!"

    def create_physical_joint(self, name, cpf, user, password, balance):
        with self.lock:
            if cpf in self.clients:
                raise Exceptions.ClientAlreadyExists

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF
            elif balance < 100:
                raise Exceptions.InvalidBalance

            new_client = PhysicalAccount.JointClient(name, cpf, user, password, agency, account)
            new_account = PhysicalAccount.JointAccount(balance)
            new_client.is_holder = True
            new_client.unity = new_account

            self.clients[cpf] = new_client
            return f"Conta conjunta para {name} criada com sucesso!"

    def create_joint_complementary(self, cpf_holder, name, cpf, user, password):
        with self.lock:
            if cpf in self.clients or cpf in self.clients[cpf_holder].accounts:
                raise Exceptions.ClientAlreadyExists
            elif cpf_holder not in self.clients:
                raise Exceptions.ClientNotFound

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            new_client = PhysicalAccount.JointClient(name, cpf, user, password, agency, account)
            new_client.is_holder = False
            account_holder = self.clients[cpf_holder].unity
            new_client.unity = account_holder

            self.clients[cpf_holder].accounts[cpf] = new_client
            self.clients[cpf] = new_client
            return f"Conta complementar para {name} criada com sucesso!"

    def create_juridic_account(self, name_company, cnpj, name, user, cpf, password, balance):
        with self.lock:
            if cnpj in self.clients:
                raise Exceptions.ClientAlreadyExists
            elif len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cnpj) != 14:
                raise Exceptions.InvalidCNPJ

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            new_client = JuridicAccount.JuridicClient(name, cpf, user, password, agency, account)
            new_account = JuridicAccount.JuridicAccount(name_company, cnpj, balance)
            new_client.is_admin = True
            new_client.unity = new_account

            new_account.accounts[cpf] = new_client
            self.clients[cnpj] = new_account

            return f"Conta jurídica admin para {name_company} criada com sucesso!"

    def create_juridic_employee(self, cnpj, name, user, cpf, password):
        with self.lock:
            if cnpj not in self.clients or cpf in self.clients[cnpj].accounts:
                raise Exceptions.ClientNotFound
            elif len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            new_client = JuridicAccount.JuridicClient(name, cpf, user, password, agency, account)
            object_admin = self.clients[cnpj]
            new_client.is_admin = False
            new_client.unity = object_admin

            self.clients[cnpj].accounts[cpf] = new_client
            self.clients[cpf] = new_client
            return f"Conta jurídica empregado para {name} criada com sucesso!"

    def get_client_by_name(self, name, type):
        for c in self.clients:
            if type == "juridic":
                if self.clients[c].type_account == type:
                    if self.clients[c].balance.name == name:
                        return self.clients[c]
            else:
                if self.clients[c].name == name:
                    return self.clients[c]
        return None

    # Método para deletar uma conta
    # Lembrete: não é possível retornar a lista pura, pois ela é um objeto, então é necessário retornar um texto
    def return_clients(self):
        text_return = ""
        for client in self.clients:
            if self.clients[client].type_account == "juridic":
                text_return += (f"\t{self.clients[client].name}, {self.clients[client].cnpj}, "
                                f"{self.clients[client].type_account}\n")
            else:
                text_return += (f"\t{self.clients[client].name}, {self.clients[client].cpf}, "
                                f"{self.clients[client].type_account}\n")
        return text_return

# ------------------------------------ Funções para as transações ------------------------------------ #

    # Método para a criação de uma chave PIX
    def create_pix_key(self, cpf_cnpj, type_account, type_key, key):
        with self.lock:
            if type_account == "juridic":
                cpf, cnpj = cpf_cnpj.split("_")
                if cnpj not in self.clients:
                    raise Exceptions.ClientNotFound
                for c in self.clients[cnpj].accounts:
                    if self.clients[cnpj].accounts[c].cpf == cpf:
                        key_pix = self.generate_key(type_key, key)
                        self.clients[cnpj].accounts[c].pix[type_key] = key_pix
                        return f"Chave PIX {type_key} para {self.clients[cnpj].accounts[c].name} criada com sucesso!"

            elif cpf_cnpj not in self.clients:
                raise Exceptions.ClientNotFound
            key_pix = self.generate_key(type_key, key)
            self.clients[cpf_cnpj].pix[type_key] = key_pix
            return f"Chave PIX {type_key} para {self.clients[cpf_cnpj].name} criada com sucesso!"

    # Método para gerar ou verificar se a chave está correta
    def generate_key(self, type, key):
        if type == "random":
            key = Utils.generate_random_key()
        elif type == "cpf_cnpj":
            if len(key) != 11:
                raise Exceptions.InvalidCPF
            elif len(key) != 14:
                raise Exceptions.InvalidCNPJ
        elif type == "email":
            if "@" not in key:
                raise Exceptions.InvalidEmail
        elif type == "phone":
            if len(key) != 11:
                raise Exceptions.InvalidPhone
        else:
            raise Exceptions.TypeKeyNotFound
        return key

    # Método para obter os dicionários com as chaves cadastradas
    def return_keys(self):
        text = ""
        for client in self.clients:
            if self.clients[client].type_account == "juridic":
                continue
            else:
                text += f"\t{self.clients[client].name}, {self.clients[client].cpf}, {self.clients[client].pix}\n"
        return text

