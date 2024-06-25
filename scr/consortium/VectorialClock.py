'''
    Descrição: Código para ordenação total de eventos em um sistema distribuídos, utilizando relógio vetorial.
'''


# Importar as bibliotecas necessárias
from threading import Lock


# Classe para relógio vetorial
class VectorClock:
    def __init__(self, num_processes, process_id):
        self.clock = [0] * num_processes
        self.process_id = process_id
        self.num_processes = num_processes
        self.lock = Lock()

    # método para incrementar o relógio
    def increment(self):
        with self.lock:
            self.clock[self.process_id] += 1
            return self.clock.copy()

    # método para atualizar o relógio
    def update(self, other_clock):
        with self.lock:
            for i in range(len(self.clock)):
                self.clock[i] = max(self.clock[i], other_clock[i])
                return self.clock.copy()

    # método para obter o relógio
    def get_time(self):
        return self.clock.copy()

    # método para definir o relógio
    def __repr__(self):
        return str(self.clock)
