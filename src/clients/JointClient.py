
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
        self.accounts_bank = {
            5551: False,
            5552: False,
            5553: False,
            5554: False,
        }
