'''
Descrição: este código contém a classe PhysicalClient, que é uma classe que representa um cliente com conta física.
'''


# Classe que representa um cliente com conta física
class PhysicalClient:
    def __init__(self, name, cpf, user, password, balance, agency, account):
        self.name = name
        self.user = user
        self.cpf = cpf
        self.password = password
        self.balance = balance
        self.agency = agency
        self.account = account
        self.type_account = "physical"
        self.pix = {
            "cpf_cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
