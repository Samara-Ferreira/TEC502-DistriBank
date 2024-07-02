'''
Descrição: este código foi criado para a ordenação total de eventos em um sistema distribuídos, utilizando relógio
vetorial.
'''

# Importar a biblioteca necessária
from threading import Lock


# Classe para relógio vetorial
class VectorialClock:
    def __init__(self, num_processes, process_id):
        self.clock = [0] * num_processes
        self.process_id = process_id
        self.num_processes = num_processes
        self.lock = Lock()

    # Método para incrementar o relógio
    def increment(self):
        with self.lock:
            self.clock[self.process_id] += 1
            return self.clock.copy()

    # Método para atualizar o relógio
    def update(self, other_clock):
        with self.lock:
            for i in range(len(self.clock)):
                self.clock[i] = max(self.clock[i], other_clock[i])
                return self.clock.copy()

    # Método para obter o tempo atual do relógio
    def get_time(self):
        return self.clock.copy()

    # étodo para definir o relógio
    def __repr__(self):
        return str(self.clock)
