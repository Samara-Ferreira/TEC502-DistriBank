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

    def insere_ordenado(self, elemento):
        """Função para inserir um novo elemento no array ordenado na posição correta"""
        pos = self.busca_binaria(elemento)
        self.queue.insert(pos, elemento)

    def busca_binaria(self, target):
        """Função para encontrar a posição correta de inserção usando busca binária"""
        left, right = 0, len(self.queue) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.queue[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
