'''
Descrição: Arquivo que contém a classe para a criação de contas conjuntas.
'''


class JointAccount:
    def __init__(self, balance, agency, account, type_account):
        self.balance = balance
        self.agency = agency
        self.account = account
        self.type_account = type_account
        self.pix = {
            "cpf-cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
        self.accounts = {}


class JointClient:
    def __init__(self, name, cpf, user, password, transaction_password):
        self.name = name
        self.cpf = cpf
        self.user = user
        self.password = password
        self.transaction_password = transaction_password
