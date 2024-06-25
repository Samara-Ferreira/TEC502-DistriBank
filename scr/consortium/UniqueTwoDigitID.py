'''
Descrição: Arquivo que contém a classe para a criação de contas de pessoas físicas.

'''


class UniqueTwoDigitID:
    def __init__(self):
        self.current_id = 0

    def generate(self):
        unique_id = self.current_id
        self.current_id += 1
        if self.current_id > 99:
            self.current_id = 0
        return str(unique_id).zfill(2)
