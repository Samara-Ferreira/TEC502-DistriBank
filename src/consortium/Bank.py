'''
Descrição: Arquivo referente a classe consortium e seus métodos, onde são definidas as funções principais do banco,
como criar conta, deletar conta, criar chave pix, depositar e sacar dinheiro, realizar transações, entre outras.

PARA ADICIONAR:
- senha de transacao
'''

# Importar as bibliotecas necessárias
import __init__
import ast
import json
import requests
import utils.Utils as Utils
import exceptions.Exceptions as Exceptions
import clients.JuridicAccount as JuridicAccount
import clients.PhysicalClient as PhysicalClient
import clients.JointClient as JointClient

from threading import Lock
#from Operations import Operations
from socket import gethostbyname, gethostname

from QueueBank import QueueBank
from VectorialClock import VectorClock
from UniqueTwoDigitID import UniqueTwoDigitID


# Máquinas do larsid
'''
[{"host": "172.16.103.1", "port": 5551},
 {"host": "172.16.103.2", "port": 5552},
 {"host": "172.16.103.3", "port": 5553},
 {"host": "172.16.103.4", "port": 5554}]
'''

# Rede local (casa)
'''
192.168.0.111
'''


class Bank:
    def __init__(self, name, port):
        self.cnpj = gethostbyname(gethostname())
        self.name = name
        self.port = port
        self.clients = {}
        #self.operations = Operations(self.port, self.cnpj)
        self.lock = Lock()

        self.operations_package = []

        self.operations = QueueBank()
        self.receive_acks = {}
        self.banks = [
            {"host": "192.168.0.111", "port": 5551}
            #{"host": "192.168.0.111", "port": 5552},
            #{"host": "192.168.0.111", "port": 5553},
            #{"host": "192.168.0.111", "port": 5554}
        ]
        #self.lock = Lock()
        self.unique_id = UniqueTwoDigitID()
        self.vector_clock = VectorClock(len(self.banks), self.banks.index({"host": self.cnpj, "port": self.port}))
        self.clients_accounts = {}
        self.lock_add = Lock()
        self.lock_exec = Lock()

    # Método para fazer login na conta
    def login(self, user, password):
        for client in self.clients:
            if self.clients[client].user == user:
                if self.clients[client].password == password:
                    return f"{self.clients[client].name};{self.clients[client].cpf};{self.clients[client].type_account}"
                raise Exceptions.InvalidPassword
        raise Exceptions.ClientNotFound

    # Método para deslogar da conta
    def logout(self, user):
        for client in self.clients:
            if self.clients[client].user == user:
                return f"Deslogado com sucesso da conta de {self.clients[client].name}!"
        raise Exceptions.ClientNotFound

    # ------------------------------------ Funções para a criação das contas ------------------------------------ #

    # Método para criar uma conta física particular
    def create_physical_particular(self, name, cpf, user, password, balance):
        with self.lock:
            if cpf+"phys" in self.clients:
                raise Exceptions.ClientAlreadyExists

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF
            elif balance < 100:
                raise Exceptions.InvalidBalance

            new_client = PhysicalClient.PhysicalClient(name, cpf, user, password, balance, agency, account)
            self.clients[cpf+"phys"] = new_client

            # Verificar se a conta existe em outros bancos
            #self.check_account(cpf+"phys")

            return f"Conta particular para {name} criada com sucesso!"

    # Método para criar uma conta física conjunta
    def create_physical_joint(self, name, cpf, user, password, balance):
        with self.lock:
            if cpf+"join" in self.clients:
                raise Exceptions.ClientAlreadyExists

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF
            elif balance < 100:
                raise Exceptions.InvalidBalance

            new_client = JointClient.JointClient(name, cpf, user, password, agency, account)
            new_account = JointClient.JointAccount(balance)
            new_client.is_holder = True
            new_client.unity = new_account
            self.clients[cpf+"join"] = new_client

            #self.check_account(cpf+"join")

            return f"Conta conjunta para {name} criada com sucesso!"

    # Método para criar uma conta física conjunta complementar
    def create_joint_complementary(self, cpf_holder, name, cpf, user, password):
        with self.lock:
            if cpf+"join" in self.clients or cpf in self.clients[cpf_holder+"join"].accounts:
                raise Exceptions.ClientAlreadyExists
            elif cpf_holder+"join" not in self.clients:
                raise Exceptions.ClientNotFound

            if len(password) < 6:
                raise Exceptions.InvalidPassword
            elif len(cpf) != 11:
                raise Exceptions.InvalidCPF

            agency, account = Utils.generate_agency_account(self.cnpj, len(self.clients))

            new_client = JointClient.JointClient(name, cpf, user, password, agency, account)
            new_client.is_holder = False
            account_holder = self.clients[cpf_holder+"join"].unity
            new_client.unity = account_holder

            self.clients[cpf_holder+"join"].accounts[cpf+"join"] = new_client
            self.clients[cpf+"join"] = new_client

            #self.check_account(cpf+"join")

            return f"Conta complementar para {name} criada com sucesso!"

    # Método para criar uma conta jurídica admin
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

            new_account.accounts[cpf+"juri"] = new_client
            self.clients[cnpj] = new_account

            #self.check_account(cpf+"juri")

            return f"Conta jurídica admin para {name_company} criada com sucesso!"

    # Método para criar uma conta jurídica empregado
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

            self.clients[cnpj].accounts[cpf+"juri"] = new_client
            self.clients[cpf+"juri"] = new_client

            #self.check_account(cpf+"juri")

            return f"Conta jurídica empregado para {name} criada com sucesso!"

    # Método para retornar a lista de contas
    # Lembrete: não é possível retornar a lista pura, pois ela é um objeto, então é necessário retornar um texto
    def get_accounts(self):
        text_return = ""
        for client in self.clients:
            if self.clients[client].type_account == "juridic_company":
                text_return += (f" | {self.clients[client].name}, {self.clients[client].cnpj}, "
                                f"{self.clients[client].type_account}, R$ {self.clients[client].balance} | ")
            elif (self.clients[client].type_account == "juridic"
                  or self.clients[client].type_account == "physical_joint"):
                text_return += (f" | {self.clients[client].name}, {self.clients[client].cpf}, {self.clients[client].unity.balance}, "
                                f"{self.clients[client].type_account} | ")
            else:
                text_return += (f" | {self.clients[client].name}, {self.clients[client].cpf}, "
                                f"{self.clients[client].type_account}, R$ {self.clients[client].balance} | ")
        return text_return


    '''# Método para fazer a request de verificação se a conta existe
    def check_account(self, cpf):
        for bank in self.operations.banks:
            # Verificar se o banco é o mesmo
            if bank["port"] == self.port:
                self.clients[cpf].accounts_bank[self.port] = True
            else:
                # Verificar se o banco está ativo
                try:
                    response = requests.get(f"http://{bank['host']}:{bank['port']}/{cpf}/exist_account")
                    if response.json():
                        self.clients[cpf].accounts_bank[bank["port"]] = True
                    else:
                        self.clients[cpf].accounts_bank[bank["port"]] = False
                # Caso o banco não esteja ativo?
                except requests.exceptions.ConnectionError:
                    self.clients[cpf].accounts_bank[bank["port"]] = False

    # Método para verificar se a conta existe no banco
    def exist_account(self, cpf):
        with self.lock:
            if cpf in self.clients:
                return True
            return False
'''
    # ------------------------------------ Funções para as transações ------------------------------------ #

    # Método para a criação de uma chave PIX
    def create_pix_key(self, cpf, type, type_key, key):
        print("TYPE ", type)
        with self.lock:
            if type == "physical":
                if cpf+"phys" not in self.clients:
                    raise Exceptions.ClientNotFound
                key_pix = self.generate_key(type_key, key)
                self.clients[cpf+"phys"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients[cpf+"phys"].name} criada com sucesso!"

            elif type == "physical_joint":
                if cpf+"join" not in self.clients:
                    raise Exceptions.ClientNotFound
                key_pix = self.generate_key(type_key, key)
                self.clients[cpf+"join"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients[cpf+"join"].name} criada com sucesso!"

            elif type == "juridic":
                if cpf+"juri" not in self.clients:
                    raise Exceptions.ClientNotFound
                key_pix = self.generate_key(type_key, key)
                self.clients[cpf+"juri"].pix[type_key] = key_pix
                return f"Chave PIX {type_key} para {self.clients[cpf+"juri"].name} criada com sucesso!"

            return f"Não foi possível criar a chave PIX para contas de empresa!"

    # Método para retornar as chaves pix de um usuário específico
    def get_keys(self, cpf):
        with self.lock:
            if cpf+"phys" in self.clients:
                return self.clients[cpf+"phys"].pix
            elif cpf+"join" in self.clients:
                return self.clients[cpf+"join"].pix
            elif cpf+"juri" in self.clients:
                return self.clients[cpf+"juri"].pix
            return f"Não foi possível encontrar as chaves PIX para o CPF {cpf}!"

    '''def return_keys(self):
        text = ""
        for client in self.clients:
            if self.clients[client].type_account == "juridic_company":
                continue
            else:
                text += (f"\t{self.clients[client].name}, {self.clients[client].cpf}, {self.clients[client].pix},"
                         f"{self.clients[client].type_account}\n")
        return text'''


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

    # Método para realizar um depósito
    def deposit(self, cpf_cnpj, type_account, key, value):
        if type_account == "physical":
            if cpf_cnpj+"phys" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"phys"].pix.values():
                raise Exceptions.KeyNotFound
            self.clients[cpf_cnpj+"phys"].balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj+"phys"].name} "
                    f"do tipo {self.clients[cpf_cnpj+"phys"].type_account}!")

        elif type_account == "physical_joint":
            if cpf_cnpj+"join" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"join"].pix.values():
                raise Exceptions.KeyNotFound
            self.clients[cpf_cnpj+"join"].unity.balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj+"join"].name} "
                    f"do tipo {self.clients[cpf_cnpj+"join"].type_account}!")

        elif type_account == "juridic":
            if cpf_cnpj+"juri" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"juri"].pix.values():
                raise Exceptions.KeyNotFound
            self.clients[cpf_cnpj+"juri"].unity.balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta do tipo "
                    f"{self.clients[cpf_cnpj+"juri"].type_account}!")

        elif type_account == "juridic_company":
            if cpf_cnpj not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj].pix.values():
                raise Exceptions.KeyNotFound
            self.clients[cpf_cnpj].balance += value
            return (f"Deposito de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj].name} do tipo "
                    f"{self.clients[cpf_cnpj].type_account}")

        return (f"Não foi possível realizar o d"
                f"eposito!")

    # Método para realizar um saque
    def withdraw(self, cpf_cnpj, type_account, key, value):
        if type_account == "physical":
            if cpf_cnpj+"phys" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"phys"].pix.values():
                raise Exceptions.KeyNotFound
            elif self.clients[cpf_cnpj+"phys"].balance < value:
                raise Exceptions.InsufficientBalance
            self.clients[cpf_cnpj+"phys"].balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj+"phys"].name} "
                    f"do tipo {self.clients[cpf_cnpj+"phys"].type_account}!")

        elif type_account == "physical_joint":
            if cpf_cnpj+"join" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"join"].pix.values():
                raise Exceptions.KeyNotFound
            elif self.clients[cpf_cnpj+"join"].unity.balance < value:
                raise Exceptions.InsufficientBalance
            self.clients[cpf_cnpj+"join"].unity.balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj+"join"].name} "
                    f"do tipo {self.clients[cpf_cnpj+"join"].type_account}!")

        elif type_account == "juridic":
            if cpf_cnpj+"juri" not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj+"juri"].pix.values():
                raise Exceptions.KeyNotFound
            elif self.clients[cpf_cnpj+"juri"].unity.balance < value:
                raise Exceptions.InsufficientBalance
            self.clients[cpf_cnpj+"juri"].unity.balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj+"juri"].name} do tipo "
                    f"{self.clients[cpf_cnpj+"juri"].type_account}!")

        elif type_account == "juridic_company":
            if cpf_cnpj not in self.clients:
                raise Exceptions.ClientNotFound
            elif key not in self.clients[cpf_cnpj].pix.values():
                raise Exceptions.KeyNotFound
            elif self.clients[cpf_cnpj].balance < value:
                raise Exceptions.InsufficientBalance
            self.clients[cpf_cnpj].balance -= value
            return (f"Saque de R${value} realizado com sucesso para uma conta {self.clients[cpf_cnpj].name} do tipo "
                    f"{self.clients[cpf_cnpj].type_account}")

        return (f"Não foi possível realizar o saque!")

    # Método para retornar o saldo
    '''def return_balances(self):
        text = ""
        for client in self.clients:
            if self.clients[client].type_account == "physical_joint" or self.clients[client].type_account == "juridic":
                text += (f"\t{self.clients[client].name}, {self.clients[client].unity.balance}, "
                         f"{self.clients[client].type_account}\n")
            else:
                text += f"\t{self.clients[client].name}, {self.clients[client].balance}, {self.clients[client].type_account}\n"
        return text'''

    # Método para retornar o saldo de uma conta específica
    def get_balance(self, cpf, type):
        if type == "physical" or "juridic_company":
            if cpf+"phys" in self.clients:
                return self.clients[cpf+"phys"].balance
        elif type == "physical_joint" or type == "juridic":
            if cpf+"join" in self.clients:
                return self.clients[cpf+"join"].unity.balance
        return f"Não foi possível encontrar o saldo da conta!"

    # ------------------------------------ Funções para as transações de fato------------------------------------ #

    # Método para criar um depósito e enviar para a fila
    def create_deposit(self, bank, cpf, type, key, value):
        op = {"bank": bank, "cpf": cpf, "type": type, "key": key, "value": value, "operation": "deposit"}
        retorno = self.add_new_operation(str([op]))
        return retorno

    # Método para criar um saque e enviar para a fila
    def create_withdraw(self, bank, cpf, type, key, value):
        op = {"bank": bank, "cpf": cpf, "type": type, "key": key, "value": value, "operation": "withdraw"}
        retorno = self.add_new_operation(str([op]))
        return retorno

    def create_transfer(self, operations):
        #list_operations = ast.literal_eval(operations)
        #print("\n\n\tNA CRIACAO TRANSFERENCIA ", list_operations, type(list_operations), "\n\n")
        retorno = self.add_new_operation(operations)
        return retorno

    # Método para criação das operações de transações
    '''def create_transfer(self, port_recp, port_send, cpf_recp, cpf_send, type_recp, type_send, key, value, same):
        op = {"recipient": port_recp, "sender": port_send, "cpf_recipient": cpf_recp, "cpf_sender": cpf_send,
            "type_recipient": type_recp, "type_sender": type_send, "key": key, "value": value,
            "operation": "transfer"}

        if same == "True":
            self.operations_package.append(op)
        else:
            self.operations_package.append(op)
            retorno = self.add_new_operation(self.operations_package)
            return retorno'''

    #def add_operations_in_packet(self, operation):
        # with self.lock_add:
        #     if self.operations_package == []:
        #         self.operations_package.append(operation)
        #         # USAR O TIMEOUT
        #         return "Operação adicionada com sucesso! Esperando por mais..."
        #     else:
        #         if operation["id"] in self.operations_package:
        #             self.operations_package.append(operation)
        #             # colocar um timeout para saber se não chega nova
        #             return "Operação nova adicionada com sucesso! Esperando por mais..."
        #         else:
        #             print("ENTROU AQUI CM QUAL OP ", operation)
        #             self.add_new_operation(self.operations_package)
        #             self.operations_package = []
        #             self.operations_package.append(operation)
        #             # COLOCAR TIMEOUT
        #             return "Operação nova adicionada!"

    # ------------------------------------ OPERAÇÕES ------------------------------------ #

    # Método para adicionar uma nova operação na fila de prioridade
    def add_new_operation(self, operation):
        with self.lock:

            list_operations = ast.literal_eval(operation)

            self.vector_clock.increment()
            time = self.vector_clock.get_time()
            port = str(self.port)

            id = port[-2:] + self.unique_id.generate()
            #op = [time, operation, id]
            op = [time, list_operations, id]

            self.operations.insert_order(op)
            self.send_new_operation(op)

            check_ack = self.check_acks()
            check_operation = self.check_list_operations(op)

            if check_ack and check_operation:
                self.execute_operation()

                if len(self.operations.queue) > 0:
                    self.execute_operation()

            return f"Operacao adicionada com sucesso!"

    # Método para verificar se a conta existe no banco
    '''def exist_account(self, cpf):
        with self.lock:
            if cpf in self.clients_accounts:
                return True
            return False
    '''

    # Método para executar uma operação da fila de prioridade
    def execute_operation(self):
        with self.lock_exec:
            for i in range(len(self.operations.queue)):

                time, operations = self.operations.queue[0][0], self.operations.queue[0][1]

                for op in operations:
                    if op["operation"] == "deposit":
                        # por que no deposito ta dando o erro 405?
                        response = requests.post(f"http://{self.cnpj}:{op['bank']}/{op['cpf']}/{op['type']}/{op['key']}"
                                                f"/{op['value']}/deposit")
                        if response.status_code != 200:
                            break

                    elif op["operation"] == "withdraw":
                        response = requests.post(f"http://{self.cnpj}:{op['bank']}/{op['cpf']}/{op['type']}/{op['key']}"
                                                f"/{op['value']}/withdraw")
                        if response.status_code != 200:
                            break

                    elif op["operation"] == "transfer":
                        # Primeiramente, faz o depósito na conta do destinatário
                        response = requests.post(f"http://{self.cnpj}:{op['recipient']}/{op['cpf_recipient']}/"
                                                f"{op['type_recipient']}/{op['key_recp']}"
                                                f"/{op['value']}/deposit")
                        if response.status_code == 200:
                            # Em seguida, faz o saque na conta do remetente
                            response = requests.post(f"http://{self.cnpj}:{op['sender']}/{op['cpf_sender']}/"
                                                    f"{op['type_sender']}/{op['key_send']}"
                                                    f"/{op['value']}/withdraw")

                            if response.status_code != 200:
                                break
                        else:
                            break

                self.delete_operations()

            return "Operações executadas com sucesso!"

    # Método para adicionar as operações executadas em cada banco
    def add_first_operation(self, operation):
        self.operations.queue_exec.append(operation)
        return "Operação adicionada com sucesso!"

    def delete_operations(self):
        # Quando retornar depois da execução...
        # Excluir a operação da fila de prioridade
        for bank in self.banks:
            response = requests.get(f"http://{bank['host']}:{bank['port']}/delete_first_operation")
            requests.get(f"http://{bank['host']}:{bank['port']}/{response.json()}/add_first_operation")

    # Método para deletar a primeira operação da fila de prioridade
    def delete_first_operation(self):
        if len(self.operations.queue) > 0:
            pop_op = self.operations.queue.pop(0)
            return pop_op

    # Método para retornar a primeira operação da fila de prioridade
    def get_first_operation(self):
        return self.operations.queue[0][0]

    # Método para verificar a lista de operações dos outros bancos
    def check_list_operations(self, operation):
        time, message = operation[0], operation[1]
        for bank in self.banks:
            if self.port == bank["port"]:
                continue
            response = requests.get(f"http://{bank['host']}:{bank['port']}/get_first_operation")
            if response.json() != time:
                return False
        return True

    # Método para enviar uma nova operação para os demais bancos
    def send_new_operation(self, operation):
        for bank in self.banks:
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
        # self.list_operations.insert_element(op)
        self.operations.insert_order(op)

        # enviar os acks para os outros bancos
        self.send_ack(message, id_message)

        return f"Operação {operation} adicionada com sucesso!"

    # Método para enviar um ack para os demais bancos
    def send_ack(self, message, id_message):
        for bank in self.banks:
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
        for bank in self.banks:
            port = bank["port"]
            id_bank = str(port)
            id_bank = id_bank[-2:]
            response = requests.get(f"http://{bank['host']}:{port}/return_ack")
            dict_acks = json.loads(response.text)
            for id in dict_acks:
                if id[:2] == id_bank:
                    if len(dict_acks[id]) != (len(self.banks) - 1):
                        return False
                elif id[:2] != id_bank:
                    if len(dict_acks[id]) != (len(self.banks) - 2):
                        return False
        return True

    # Método para retornar os acks do banco
    def return_acks(self):
        return self.receive_acks

    # Método para retornar a fila de prioridade do banco
    def return_queues(self):
        return f"Fila do banco {self.port}: {self.operations.queue}"

    # Método para retornar as operações executadas
    def get_queue_executed(self):
        return f"Operações executadas do banco {self.port}: {self.operations.queue_exec}"

