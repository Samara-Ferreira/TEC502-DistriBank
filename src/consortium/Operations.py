'''
Descrição: Arquivo referente a classe de operações do banco, onde são criadas as listas e suas operações.
'''

# Importar as bibliotecas necessárias
import ast
import json
import requests

from threading import Lock
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


class Operations:
    # Definir as listas de operações
    def __init__(self, port, cnpj):
        self.cnpj = cnpj
        self.port = port
        self.operations = QueueBank()
        self.receive_acks = {}
        self.banks = [
            {"host": "192.168.0.111", "port": 5551},
            {"host": "192.168.0.111", "port": 5552},
            {"host": "192.168.0.111", "port": 5553},
            {"host": "192.168.0.111", "port": 5554}
        ]
        self.lock = Lock()
        self.unique_id = UniqueTwoDigitID()
        self.vector_clock = VectorClock(len(self.banks), self.banks.index({"host": self.cnpj, "port": self.port}))

    # Método para adicionar uma nova operação na fila de prioridade
    def add_new_operation(self, operation):
        with self.lock:
            self.vector_clock.increment()
            time = self.vector_clock.get_time()
            port = str(self.port)

            id = port[-2:] + self.unique_id.generate()

            op = [time, operation, id]

            self.operations.insert_order(op)
            self.send_new_operation(op)

            check_ack = self.check_acks()
            check_operation = self.check_list_operations(op)

            if check_ack and check_operation:
                self.execute_operation()

                if len(self.operations.queue) > 0:
                    self.execute_operation()

            return f"Operacao {operation} adicionada com sucesso!", check_ack, check_operation

    # Método para executar uma operação da fila de prioridade
    def execute_operation(self):
        for i in range(len(self.operations.queue)):
            time, message = self.operations.queue[0][0], self.operations.queue[0][1]
            # Código para executar as operações... aqui que eu coloco em uma thread?
            if message == "deposit":
                print("Executando um depósito....")
            else:
                print("Outra operação...")
            # Quando retornar depois da execução...
            # Excluir a operação da fila de prioridade
            for bank in self.banks:
                response = requests.get(f"http://{bank['host']}:{bank['port']}/delete_first_operation")
                requests.get(f"http://{bank['host']}:{bank['port']}/{response.json()}/add_first_operation")
        return "Operações executadas com sucesso!"

    # Método para adicionar as operações executadas em cada banco
    def add_first_operation(self, operation):
        self.operations.queue_exec.append(operation)
        return "Operação adicionada com sucesso!"

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
    def return_executed(self):
        return f"Operações executadas do banco {self.port}: {self.operations.queue_exec}"

