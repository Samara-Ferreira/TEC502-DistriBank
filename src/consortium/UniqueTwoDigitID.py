'''
Descrição: este código contém a classe para a criação de um identificador único de dois dígitos
para as operações do banco.
'''


# Classe para a criação de um identificador único de dois dígitos
class UniqueTwoDigitID:
    def __init__(self):
        self.current_id = 0

    # Método para gerar um identificador único
    def generate(self):
        unique_id = self.current_id
        self.current_id += 1
        if self.current_id > 99:
            self.current_id = 0
        return str(unique_id).zfill(2)
