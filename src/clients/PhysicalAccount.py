'''
Descrição: Arquivo que contém a Classe para a criação de contas de pessoas físicas.
'''


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


class JointAccount:
    def __init__(self, balance):
        self.balance = balance


class JointClient:
    def __init__(self, name, cpf, user, password, agency, account):
        self.name = name
        self.cpf = cpf
        self.user = user
        self.unity = None
        self.password = password
        self.agency = agency
        self.account = account
        self.is_holder = None
        self.type_account = "physical_joint"
        self.accounts = {}
        self.pix = {
            "cpf_cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
