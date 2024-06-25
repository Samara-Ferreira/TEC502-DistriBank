'''
Descrição: Arquivo que contém a classe para a criação de contas de pessoas jurídicas.
'''


class JuridicAccount:
    def __init__(self, name, user, cnpj, password, balance, agency, account, transaction_password, type_account):
        self.name = name
        self.user = user
        self.cnpj = cnpj
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
        self.accounts = {}


class JuridicClient:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password
