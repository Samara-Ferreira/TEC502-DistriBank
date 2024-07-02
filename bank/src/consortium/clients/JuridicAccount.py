'''
Descrição: este código contém a classe JuridicAccount, que é uma classe que representa uma conta jurídica.
'''


# Classe que representa uma conta jurídica
class JuridicAccount:
    def __init__(self, name, cnpj, balance):
        self.name = name
        self.cnpj = cnpj
        self.balance = balance
        self.accounts = {}
        self.type_account = "juridic_company"


# Classe que representa um cliente com conta jurídica
class JuridicClient:
    def __init__(self, name, cpf, user, password, agency, account):
        self.name = name
        self.cpf = cpf
        self.user = user
        self.password = password
        self.agency = agency
        self.account = account
        self.unity = None
        self.is_admin = None
        self.type_account = "juridic"
        self.pix = {
            "cpf_cnpj": None,
            "email": None,
            "phone": None,
            "random": None
        }
