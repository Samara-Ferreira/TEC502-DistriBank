'''
Descrição: este código contém a classe Bank, que é responsável por gerenciar as contas dos clientes no sistema bancário.
'''

# Importar as bibliotecas necessárias
import ast
import time
import json
import socket
import requests

from Queue import Queue
from utils import Utils
from exceptions import Exceptions
from threading import Lock, Thread
from VectorialClock import VectorialClock
from socket import gethostbyname, gethostname
from UniqueTwoDigitID import UniqueTwoDigitID
from clients import PhysicalClient, JointClient, JuridicAccount


# Classe que gerencia as contas dos clientes no sistema bancário
class Bank:
    def __init__(self, port):
        self.port = port
        self.cnpj = gethostbyname(gethostname())
        self.clients_accounts = {}
        self.lock = Lock()
        self.queue_operations = Queue()
        self.unique_id = UniqueTwoDigitID()
        self.banks = [
            {"host": "172.16.103.1", "port": 5551, "active": True},
            {"host": "172.16.103.2", "port": 5552, "active": True},
            {"host": "172.16.103.4", "port": 5553, "active": True},
            {"host": "172.16.103.5", "port": 5554, "active": True}
        ]
        # self.banks = [
        #     {"host": "192.168.0.111", "port": 5551, "active": True},
        #     {"host": "192.168.0.111", "port": 5552, "active": True},
        #     {"host": "192.168.0.111", "port": 5553, "active": True},
        #     {"host": "192.168.0.111", "port": 5554, "active": True}
        # ]
        self.vector_clock = VectorialClock(len(self.banks), self.banks.index({"host": self.cnpj,
                                                                              "port": self.port, "active": True}))
        self.lock_exec = Lock()
        self.lock_create = Lock()
        self.receive_acks = {}
        self.thread_active = Thread(target=self.check_server, args=()).start()

    # Método para fazer login na conta
    def login(self, type, user, password):
        for client in self.clients_accounts:
            if self.clients_accounts[client].type_account == type:
                if self.clients_accounts[client].user == user:
                    if self.clients_accounts[client].password == password:
                        return (f"{self.clients_accounts[client].name};{self.clients_accounts[client].cpf};"
                                f"{self.clients_accounts[client].type_account}")
                    raise Exceptions.InvalidPassword
        raise Exceptions.ClientNotFound

    # Método para deslogar da conta
    def logout(self, user):
        for client in self.clients_accounts:
            if self.clients_accounts[client].type_account == "juridic_company":
                continue
            if self.clients_accounts[client].user == user:
                return f"Deslogado com sucesso da conta de {self.clients_accounts[client].name}!"
        raise Exceptions.ClientNotFound

    # Método para criar uma conta física particular
    def create_physical_particular(self, name, cpf, user, password, balance):
        with self.lock_create:
            if cpf+"phys" in self.clients_accounts:
                raise Exceptions.ClientAlreadyExists

            agency, account = self.generate_agency_account()

            new_client = PhysicalClient.PhysicalClient(name, cpf, user, password, balance, agency, account)
            self.clients_accounts[cpf+"phys"] = new_client
            return f"Conta particular para {name} criada com sucesso!"

    # Método para criar uma conta física conjunta
    def create_physical_joint(self, name, cpf, user, password, balance):
        with self.lock_create:
            if cpf+"join" in self.clients_accounts:
                raise Exceptions.ClientAlreadyExists

            agency, account = self.generate_agency_account()

            new_client = JointClient.JointClient(name, cpf, user, password, agency, account)
            new_account = JointClient.JointAccount(balance)
            new_client.is_holder = True
            new_client.unity = new_account
            self.clients_accounts[cpf+"join"] = new_client
            return f"Conta conjunta para {name} criada com sucesso!"

    # Método para criar uma conta física conjunta complementar
    def create_joint_complementary(self, cpf_holder, name, cpf, user, password):
        with self.lock_create:
            if cpf_holder+"join" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            if cpf+"join" in self.clients_accounts[cpf_holder+"join"].accounts:
                raise Exceptions.ClientAlreadyExists

            agency, account = self.generate_agency_account()

            new_client = JointClient.JointClient(name, cpf, user, password, agency, account)
            new_client.is_holder = False
            account_holder = self.clients_accounts[cpf_holder+"join"].unity
            new_client.unity = account_holder

            self.clients_accounts[cpf_holder+"join"].accounts[cpf+"join"] = new_client
            self.clients_accounts[cpf+"join"] = new_client
            return f"Conta complementar para {name} criada com sucesso!"

    # Método para criar uma conta jurídica admin
    def create_juridic_account(self, name_company, cnpj, name, user, cpf, password, balance):
        with self.lock_create:
            if cnpj in self.clients_accounts:
                raise Exceptions.ClientAlreadyExists

            agency, account = self.generate_agency_account()

            new_client = JuridicAccount.JuridicClient(name, cpf, user, password, agency, account)
            new_account = JuridicAccount.JuridicAccount(name_company, cnpj, balance)
            new_client.is_admin = True
            new_client.unity = new_account

            new_account.accounts[cpf+"juri"] = new_client
            self.clients_accounts[cnpj] = new_account
            self.clients_accounts[cpf+"juri"] = new_client
            return f"Conta jurídica (admin) para {name_company} criada com sucesso!"

    # Método para criar uma conta jurídica empregado
    def create_juridic_employee(self, cnpj, name, user, cpf, password):
        with self.lock_create:
            if cnpj not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            elif cpf+"juri" in self.clients_accounts:
                raise Exceptions.ClientAlreadyExists

            agency, account = self.generate_agency_account()

            new_client = JuridicAccount.JuridicClient(name, cpf, user, password, agency, account)
            object_admin = self.clients_accounts[cnpj]
            new_client.is_admin = False
            new_client.unity = object_admin

            self.clients_accounts[cnpj].accounts[cpf+"juri"] = new_client
            self.clients_accounts[cpf+"juri"] = new_client
            return f"Usuário {name} adicionado à conta jurídica com sucesso!"

    # Método para gerar a agência e o número da conta de um cliente
    def generate_agency_account(self):
        return Utils.generate_agency_account(self.cnpj, len(self.clients_accounts))

    # Método para verificar se a chave existe
    def check_key(self, key):
        for client in self.clients_accounts:
            if self.clients_accounts[client].type_account == "juridic_company":
                continue
            if key in self.clients_accounts[client].pix.values():
                return "True"
        return "False"

    # Método para a criação de uma chave PIX
    def create_pix_key(self, cpf, type, type_key, key):
        with self.lock:
            if type == "physical":
                if cpf+"phys" not in self.clients_accounts:
                    raise Exceptions.ClientNotFound

                elif self.clients_accounts[cpf+"phys"].pix[type_key] is not None:
                    raise Exceptions.KeyAlreadyExists

                key_pix = self.generate_key(type_key, key)
                self.clients_accounts[cpf+"phys"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients_accounts[cpf+"phys"].name} criada com sucesso!"

            elif type == "physical_joint":
                if cpf+"join" not in self.clients_accounts:
                    raise Exceptions.ClientNotFound

                elif self.clients_accounts[cpf+"join"].pix[type_key] is not None:
                    raise Exceptions.KeyAlreadyExists

                key_pix = self.generate_key(type_key, key)
                self.clients_accounts[cpf+"join"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients_accounts[cpf+"join"].name} criada com sucesso!"

            elif type == "juridic":
                if cpf+"juri" not in self.clients_accounts:
                    raise Exceptions.ClientNotFound

                elif self.clients_accounts[cpf+"juri"].pix[type_key] is not None:
                    raise Exceptions.KeyAlreadyExists

                key_pix = self.generate_key(type_key, key)
                self.clients_accounts[cpf+"juri"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients_accounts[cpf+"juri"].name} criada com sucesso!"
            raise Exceptions.ClientNotFound

    # Método para gerar ou verificar se a chave está correta
    def generate_key(self, type, key):
        if type == "random":
            key = Utils.generate_random_key()
        elif type == "cpf_cnpj":
            if len(key) != 11:
                raise Exceptions.InvalidKey
            elif len(key) != 14:
                raise Exceptions.InvalidKey
        elif type == "email":
            if "@" not in key:
                raise Exceptions.InvalidKey
        elif type == "phone":
            if len(key) != 11:
                raise Exceptions.InvalidKey
        else:
            raise Exceptions.InvalidKey
        return key

    # Método para retornar as chaves pix de um usuário específico
    def get_keys(self, cpf, type):
        if type == "physical":
            if cpf+"phys" in self.clients_accounts:
                return self.clients_accounts[cpf+"phys"].pix

        elif type == "physical_joint":
            if cpf+"join" in self.clients_accounts:
                return self.clients_accounts[cpf+"join"].pix

        elif type == "juridic":
            if cpf+"juri" in self.clients_accounts:
                return self.clients_accounts[cpf+"juri"].pix
        raise Exceptions.ClientNotFound

    # Método para retornar o saldo de uma conta específica
    def get_balance(self, cpf, type):
        if type == "physical":
            if cpf+"phys" in self.clients_accounts:
                return self.clients_accounts[cpf+"phys"].balance

        elif type == "physical_joint":
            if cpf+"join" in self.clients_accounts:
                return self.clients_accounts[cpf+"join"].unity.balance

        elif type == "juridic":
            if cpf+"juri" in self.clients_accounts:
                return self.clients_accounts[cpf+"juri"].unity.balance
        raise Exceptions.ClientNotFound

    # Método para retornar a lista de clientes
    def get_clients(self):
        if len(self.clients_accounts) == 0:
            raise Exceptions.ClientNotFound
        clients = []
        for client in self.clients_accounts:
            if self.clients_accounts[client].type_account == "juridic_company":
                clients.append([self.clients_accounts[client].name, self.clients_accounts[client].cnpj,
                               self.clients_accounts[client].type_account])
            else:
                clients.append([self.clients_accounts[client].name, self.clients_accounts[client].cpf,
                                self.clients_accounts[client].type_account])
        return str(clients)

    # ------------------------------------------------------------------------------------------------------------ #

    # Método para criar uma transferência
    def create_transfer(self, operations):
        return_transfer = self.add_new_operation(operations)
        return return_transfer

    # Método para criar um depósito
    def create_deposit(self, host, port, cpf, type, value):
        op = {"host": host, "port": port, "cpf": cpf, "type": type, "value": value, "operation": "deposit"}
        return_deposit = self.add_new_operation(str([op]))
        return return_deposit

    # Método para criar um saque
    def create_withdraw(self, host, port, cpf, type, value):
        op = {"host": host, "port": port, "cpf": cpf, "type": type, "value": value, "operation": "withdraw"}
        return_withdraw = self.add_new_operation(str([op]))
        return return_withdraw

    # Método para realizar um depósito
    def deposit(self, cpf_cnpj, type_account, key, value):
        if type_account == "physical":
            if cpf_cnpj+"phys" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"phys"].pix.values():
                raise Exceptions.KeyNotFound

            self.clients_accounts[cpf_cnpj+"phys"].balance += value
            return (f"Deposito de R$ {value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"phys"].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj+"phys"].type_account}!")

        elif type_account == "physical_joint":
            if cpf_cnpj+"join" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"join"].pix.values():
                raise Exceptions.KeyNotFound

            self.clients_accounts[cpf_cnpj+"join"].unity.balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"join"].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj+"join"].type_account}!")

        elif type_account == "juridic":
            if cpf_cnpj+"juri" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"juri"].pix.values():
                raise Exceptions.KeyNotFound

            self.clients_accounts[cpf_cnpj+"juri"].unity.balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"juri"].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj+"juri"].type_account}!")

        elif type_account == "juridic_company":
            if cpf_cnpj not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj].pix.values():
                raise Exceptions.KeyNotFound

            self.clients_accounts[cpf_cnpj].balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj].type_account}")
        raise Exceptions.ClientNotFound

    # Método para realizar um depósito interno
    def in_deposit(self, cpf, type, value):
        if type == "physical":
            if cpf+"phys" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"phys"].balance += value
            return f"Depósito de R$ {value} realizado com sucesso!"

        elif type == "physical_joint":
            if cpf+"join" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"join"].unity.balance += value
            return f"Depósito de R$ {value} realizado com sucesso!"

        elif type == "juridic":
            if cpf+"juri" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"juri"].unity.balance += value
            return f"Depósito de R$ {value} realizado com sucesso!"

        elif type == "juridic_company":
            if cpf not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf].balance += value
            return f"Depósito de R$ {value} realizado com sucesso!"
        return "Nulo"

    # Método para realizar um saque
    def withdraw(self, cpf_cnpj, type_account, key, value):
        # Verificar se tem saldo suficiente
        actual_balance = self.get_balance(cpf_cnpj, type_account)
        if actual_balance < value:
            raise Exceptions.InsufficientBalance

        if type_account == "physical":
            if cpf_cnpj+"phys" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"phys"].pix.values():
                raise Exceptions.KeyNotFound

            elif self.clients_accounts[cpf_cnpj+"phys"].balance < value:
                raise Exceptions.InsufficientBalance

            self.clients_accounts[cpf_cnpj+"phys"].balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"phys"].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj+"phys"].type_account}!")

        elif type_account == "physical_joint":
            if cpf_cnpj+"join" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"join"].pix.values():
                raise Exceptions.KeyNotFound

            elif self.clients_accounts[cpf_cnpj+"join"].unity.balance < value:
                raise Exceptions.InsufficientBalance

            self.clients_accounts[cpf_cnpj+"join"].unity.balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"join"].name} "
                    f"do tipo {self.clients_accounts[cpf_cnpj+"join"].type_account}!")

        elif type_account == "juridic":
            if cpf_cnpj+"juri" not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj+"juri"].pix.values():
                raise Exceptions.KeyNotFound

            elif self.clients_accounts[cpf_cnpj+"juri"].unity.balance < value:
                raise Exceptions.InsufficientBalance

            self.clients_accounts[cpf_cnpj+"juri"].unity.balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj+"juri"].name} do tipo "
                    f"{self.clients_accounts[cpf_cnpj+"juri"].type_account}!")

        elif type_account == "juridic_company":
            if cpf_cnpj not in self.clients_accounts:
                raise Exceptions.ClientNotFound

            elif key not in self.clients_accounts[cpf_cnpj].pix.values():
                raise Exceptions.KeyNotFound

            elif self.clients_accounts[cpf_cnpj].balance < value:
                raise Exceptions.InsufficientBalance

            self.clients_accounts[cpf_cnpj].balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta "
                    f"{self.clients_accounts[cpf_cnpj].name} do tipo "
                    f"{self.clients_accounts[cpf_cnpj].type_account}")
        raise Exceptions.ClientNotFound

    # Método para realizar um depósito interno
    def in_withdraw(self, cpf, type, value):
        actual_balance = self.get_balance(cpf, type)
        if actual_balance < value:
            raise Exceptions.InsufficientBalance

        if type == "physical":
            if cpf+"phys" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"phys"].balance -= value
            return f"Saque de R$ {value} realizado com sucesso!"

        elif type == "physical_joint":
            if cpf+"join" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"join"].unity.balance -= value
            return f"Saque de R$ {value} realizado com sucesso!"

        elif type == "juridic":
            if cpf+"juri" not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf+"juri"].unity.balance -= value
            return f"Saque de R$ {value} realizado com sucesso!"

        elif type == "juridic_company":
            if cpf not in self.clients_accounts:
                raise Exceptions.ClientNotFound
            self.clients_accounts[cpf].balance -= value
            return f"Saque de R$ {value} realizado com sucesso!"
        raise Exceptions.ClientNotFound

    # ------------------------------------------------------------------------#

    # Método para adicionar uma nova operação na fila de prioridade
    def add_new_operation(self, operation):
        with self.lock:

            # Verifica se um dos bancos está inativo
            for bank in self.banks:
                if bank["active"] is False:
                    return f"Banco {bank} inativo!"

            # Transformar a string em uma lista (pode possuir mais de uma operação)
            list_operations = ast.literal_eval(operation)

            # Incrementar o relógio vetorial e obter o tempo atual
            self.vector_clock.increment()
            time = self.vector_clock.get_time()
            port = str(self.port)

            # Gerar um id único para a operação
            id = port[-2:] + self.unique_id.generate()
            op = [time, list_operations, id]

            # Adicionar a operação na fila de prioridade
            self.queue_operations.insert_order(op)

            # Enviar a operação para os demais bancos
            self.send_new_operation(op)

            # Verificar se o número de acks está correto e se a operação é a primeira da fila em todos os bancos
            check_ack = self.check_acks()
            check_operation = self.check_list_operations(op)

            # Se os acks estiverem corretos e a operação for a primeira da fila em todos os bancos, executar a operação
            if check_ack and check_operation:
                self.execute_operations()

                # Executar enquanto houver operações na fila de prioridade
                if len(self.queue_operations.queue) > 0:
                    self.execute_operations()

            return f"Operações na fila executadas!"

    # Método para executar uma operação da fila de prioridade
    def execute_operations(self):
        with self.lock_exec:
            for i in range(len(self.queue_operations.queue)):

                time, operations = self.queue_operations.queue[0][0], self.queue_operations.queue[0][1]

                return_semi_exec = self.semi_execute_operations(operations)

                if return_semi_exec is True:
                    for op in operations:
                        # Antes de executar, verifica se o banco está ativo
                        if op["operation"] == "deposit":
                            requests.post(f"http://{op['host']}:{op['port']}/{op['cpf']}/{op['type']}"
                                                     f"/{op['value']}/in_deposit")

                        elif op["operation"] == "withdraw":
                            requests.post(f"http://{op['host']}:{op['port']}/{op['cpf']}/{op['type']}"
                                                     f"/{op['value']}/in_withdraw")

                        elif op["operation"] == "transfer":
                            requests.post(f"http://{op['host_send']}:{op['port_send']}/{op['cpf_send']}"
                                                     f"/{op['type_send']}/{op['value']}/in_withdraw")

                            requests.post(f"http://{op['host_recp']}:{op['port_recp']}/{op['cpf_recp']}"
                                                         f"/{op['type_recp']}/{op['key_recp']}"
                                                         f"/{op['value']}/deposit")

                self.delete_operations()

            return "Operações executadas com sucesso!"

    # Função para verificar quando o servidor for ativado, para limpar a fila dele
    # def delete_queue_servers(self, port):
    #     for bank in self.banks:
    #         if bank["port"] == port:
    #             continue
    #         requests.get(f"http://{bank['host']}:{bank['port']}/delete_queue")
    #
    # def delete_queue_return(self, host, port):
    #     requests.get(f"http://{host}:{port}/delete_queue")
    #
    # def try_delete_queue(self, index):
    #     while True:
    #         if self.banks[index]["active"] is True:
    #             self.delete_queue_return(self.banks[index]["host"], self.banks[index]["port"])
    #             break
    #         time.sleep(1)
    #
    # def delete_queue(self):
    #     if len(self.queue_operations.queue) > 0:
    #         self.queue_operations.queue = []

    # Método para verificar se as operações podem ser executadas
    def semi_execute_operations(self, operations):
        for op in operations:
            # Antes de executar, verifica se o banco está ativo
            if op["operation"] == "deposit":
                for bank in self.banks:
                    if bank["active"] is False:
                        if bank["port"] == op["port"]:
                            # self.delete_queue_servers(op["port"])
                            # # Pega o índice como args da Thread
                            # index = self.banks.index(bank)
                            # Thread(target=self.try_delete_queue, args=(index,)).start()
                            return False
                value = 0.0
                response = requests.post(f"http://{op['host']}:{op['port']}/{op['cpf']}/{op['type']}"
                                         f"/{value}/in_deposit")
                if response.status_code != 200:
                    return False

            elif op["operation"] == "withdraw":
                for bank in self.banks:
                    if bank["active"] is False:
                        if bank["port"] == op["port"]:
                            # self.delete_queue_servers(op["port"])
                            # # Pega o índice como args da Thread
                            # index = self.banks.index(bank)
                            # Thread(target=self.try_delete_queue, args=(index,)).start()
                            return False
                value = 0.0
                response = requests.post(f"http://{op['host']}:{op['port']}/{op['cpf']}/{op['type']}"
                                         f"/{value}/in_withdraw")
                if response.status_code != 200:
                    return False

            elif op["operation"] == "transfer":
                for bank in self.banks:
                    if bank["active"] is False:
                        if bank["port"] == op["port_send"]:
                            # self.delete_queue_servers(op["port"])
                            # # Pega o índice como args da Thread
                            # index = self.banks.index(bank)
                            # Thread(target=self.try_delete_queue, args=(index,)).start()
                            return False

                for bank in self.banks:
                    if bank["active"] is False:
                        if bank["port"] == op["port_recp"]:
                            # self.delete_queue_servers(op["port"])
                            # # Pega o índice como args da Thread
                            # index = self.banks.index(bank)
                            # Thread(target=self.try_delete_queue, args=(index,)).start()
                            return False
                value = 0.0

                response = requests.post(f"http://{op['host_send']}:{op['port_send']}/{op['cpf_send']}"
                                         f"/{op['type_send']}/{value}/in_withdraw")
                if response.status_code == 200:
                    value = 0.0
                    response = requests.post(f"http://{op['host_recp']}:{op['port_recp']}/{op['cpf_recp']}"
                                             f"/{op['type_recp']}/{op['key_recp']}"
                                             f"/{value}/deposit")

                    if response.status_code != 200:
                        return False
                else:
                    return False
        return True

    # Método para deletar as operações executadas em cada um dos bancos
    def delete_operations(self):
        # Quando retornar depois da execução...
        # Excluir a operação da fila de prioridade
        for bank in self.banks:
            if bank["active"] is False:
                continue

            response = requests.get(f"http://{bank['host']}:{bank['port']}/delete_first_operation")
            requests.get(f"http://{bank['host']}:{bank['port']}/{response.json()}/add_first_operation")

    # Método para adicionar as operações executadas em cada banco
    def add_first_operation(self, operation):
        self.queue_operations.queue_exec.append(operation)
        return "Operação adicionada com sucesso!"

    # Método para deletar a primeira operação da fila de prioridade
    def delete_first_operation(self):
        if len(self.queue_operations.queue) > 0:
            pop_op = self.queue_operations.queue.pop(0)
            return pop_op
        return "Fila de prioridade vazia!"

    # Método para verificar a lista de operações dos outros bancos
    def check_list_operations(self, operation):
        time, message = operation[0], operation[1]
        for bank in self.banks:
            if bank["active"] is False:
                continue

            if self.port == bank["port"]:
                continue
            response = requests.get(f"http://{bank['host']}:{bank['port']}/get_first_operation")
            if response.json() != time:
                return False
        return True

    # Método para retornar a primeira operação da fila de prioridade
    def get_first_operation(self):
        return self.queue_operations.queue[0][0]

    # Método para enviar uma nova operação para os demais bancos
    def send_new_operation(self, operation):
        for bank in self.banks:
            if bank["active"] is False:
                continue

            if self.port == bank["port"]:
                continue
            requests.get(f"http://{bank['host']}:{bank['port']}/{operation}/receive_new_operation")

    # Método para receber uma nova operação de outro banco
    def receive_new_operation(self, operation):
        list_operation = ast.literal_eval(operation)

        time = list_operation[0]
        message = list_operation[1]
        id_message = list_operation[2]

        self.vector_clock.update(time)
        op = [time, message, id_message]
        self.queue_operations.insert_order(op)

        # Enviar os acks para os outros bancos
        self.send_ack(message, id_message)

        return f"Operação {operation} adicionada com sucesso!"

    # Método para enviar um ack para os demais bancos
    def send_ack(self, message, id_message):
        for bank in self.banks:
            if bank["active"] is False:
                continue

            if self.port == bank["port"]:
                continue
            ack = f"{message};OK;{id_message}"
            requests.get(f"http://{bank['host']}:{bank['port']}/{ack}/receive_ack")

    # Método para receber um ack de outro banco
    def receive_ack(self, ack):
        message, ack, id = ack.split(";")
        ack_in = [message, ack]
        if id not in self.receive_acks:
            self.receive_acks[id] = []
            self.receive_acks[id].append(ack_in)
        else:
            self.receive_acks[id].append(ack_in)
        return "ACK recebido com sucesso!"

    # Método para verificar se todos os acks foram recebidos
    def check_acks(self):
        # Verifica o número de bancos ativos
        count_banks = len(self.banks)

        for bank in self.banks:
            if bank["active"] is False:
                count_banks -= 1
                continue
            port = bank["port"]
            id_bank = str(port)
            id_bank = id_bank[-2:]
            response = requests.get(f"http://{bank['host']}:{port}/get_acks")
            dict_acks = json.loads(response.text)

            for id in dict_acks:
                if id[:2] == id_bank:
                    # if len(dict_acks[id]) != (len(self.banks) - 1):
                    if len(dict_acks[id]) != (count_banks - 1):
                        return False
                elif id[:2] != id_bank:
                    # if len(dict_acks[id]) != (len(self.banks) - 2):
                    if len(dict_acks[id]) != (count_banks - 2):
                        return False
        return True

    # Método para retornar os acks do banco
    def get_acks(self):
        return self.receive_acks

    # Método para retornar a fila de prioridade do banco
    def get_queue(self):
        return f"Fila do banco {self.port}: {self.queue_operations.queue}"

    # Método para retornar as operações executadas
    def get_queue_executed(self):
        if len(self.queue_operations.queue_exec) == 0:
            raise Exceptions.QueueIsEmpty
        return self.queue_operations.queue_exec

    # Método para checar se o cliente existe
    def check_client(self, cpf, type):
        if type == "physical":
            if cpf+"phys" in self.clients_accounts:
                return True
        elif type == "physical_joint":
            if cpf+"join" in self.clients_accounts:
                return True
        elif type == "juridic":
            if cpf+"juri" in self.clients_accounts:
                return True
        raise Exceptions.ClientNotFound

    # Método para checar se o servidor está ativo
    def check_server(self):
        while True:
            for bank in self.banks:
                try:
                    timeout = 1
                    # Cria um novo socket
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # Define um tempo limite para a tentativa de conexão
                    sock.settimeout(timeout)
                    # Tenta se conectar ao servidor
                    sock.connect((bank["host"], bank["port"]))
                    # Fecha o socket
                    sock.close()
                    self.banks[self.banks.index(bank)]["active"] = True
                except (socket.timeout, socket.error):
                    self.banks[self.banks.index(bank)]["active"] = False

            time.sleep(5)
