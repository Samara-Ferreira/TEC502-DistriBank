'''
Descrição: este código contém a classe JointClient, que é uma classe que representa um cliente com conta conjunta.
'''


# Classe que representa uma conta conjunta
class JointAccount:
    def __init__(self, balance):
        self.balance = balance


# Classe que representa um cliente com conta conjunta
class JointClient:
    def __init__(self, name, cpf, user, password, agency, account):
        self.name = name
        self.cpf = cpf
        self.user = user
        self.password = password
        self.agency = agency
        self.account = account
        self.unity = None
        self.is_holder = None
        self.type_account = "physical_joint"
        self.accounts = {}
        self.pix = {
            "cpf_cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
