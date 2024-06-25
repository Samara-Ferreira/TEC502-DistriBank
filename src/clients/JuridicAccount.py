'''
Descrição: Arquivo que contém a classe para a criação de contas de pessoas jurídicas.
'''


class JuridicAccount:
    def __init__(self, name, cnpj, balance):
        self.name = name
        self.cnpj = cnpj
        self.balance = balance
        self.accounts = {}
        self.type_account = "juridic"


class JuridicClient:
    def __init__(self, name, cpf, user, password, agency, account):
        self.name = name
        self.cpf = cpf
        self.user = user
        self.unity = None
        self.password = password
        self.agency = agency
        self.account = account
        self.is_admin = None
        self.type_account = "juridic_person"
        self.pix = {
            "cpf-cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
