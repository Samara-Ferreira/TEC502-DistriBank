
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
        self.accounts_bank = {
            5551: False,
            5552: False,
            5553: False,
            5554: False,
        }
