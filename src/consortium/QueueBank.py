'''
Descrição: Arquivo referente à fila de prioridade do banco financeiro, onde são definidas as funções principais
da fila, como inserir um elemento na fila, ordenar a fila, e comparar elementos da fila.
'''


# Classe para a fila de prioridade
class QueueBank:
    def __init__(self):
        self.lenght = 0
        self.queue = []
        self.queue_exec = []

    def insert_order(self, operation):
        pos = self.binary_search(operation)
        self.queue.insert(pos, operation)
        self.lenght += 1

    def binary_search(self, operation):
        left, right = 0, len(self.queue) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.queue[mid] < operation:
                left = mid + 1
            else:
                right = mid - 1
        return left
