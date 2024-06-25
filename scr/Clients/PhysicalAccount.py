'''
Descrição: Arquivo que contém a Classe para a criação de contas de pessoas físicas.
'''


class PhysicalClient:
    def __init__(self, name, user, cpf, password, balance, agency, account, transaction_password, type_account):
        self.name = name
        self.user = user
        self.cpf = cpf
        self.password = password
        self.balance = balance
        self.agency = agency
        self.account = account
        self.transaction_password = transaction_password
        self.type_account = type_account
        self.pix = {
            "cpf-cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
