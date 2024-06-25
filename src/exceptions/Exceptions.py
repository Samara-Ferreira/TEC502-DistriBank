'''
Descrição: Arquivo que contém as exceções personalizadas.
'''


class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Exceção: {self.message}"


# ------------------------------------ Exceções para a criação de contas ------------------------------------ #

class ClientAlreadyExists(MyException):
    def __init__(self):
        super().__init__("Cliente já existe.")


class InvalidType(MyException):
    def __init__(self):
        super().__init__("Tipo inválido.")


class InvalidCPF(MyException):
    def __init__(self):
        super().__init__("CPF inválido.")


class InvalidBalance(MyException):
    def __init__(self):
        super().__init__("Saldo inválido.")


class InvalidPassword(MyException):
    def __init__(self):
        super().__init__("Senha inválida.")


class InvalidCNPJ(MyException):
    def __init__(self):
        super().__init__("CNPJ inválido.")


class ClientNotFound(MyException):
    def __init__(self):
        super().__init__("Cliente não encontrado.")


# ------------------------------------ Exceções para as operações ------------------------------------ #
class ErrorAddingOperation(MyException):
    def __init__(self):
        super().__init__("Erro ao adicionar operação.")


class ErrorDeletingOperation(MyException):
    def __init__(self):
        super().__init__("Erro ao deletar operação.")


class ErrorSendingOperation(MyException):
    def __init__(self):
        super().__init__("Erro ao enviar operação.")


class ErrorSendingACK(MyException):
    def __init__(self):
        super().__init__("Erro ao enviar ACK.")


class ErrorReceiveACK(MyException):
    def __init__(self):
        super().__init__("Erro ao receber ACK.")


class CountACKs(MyException):
    def __init__(self):
        super().__init__("Erro ao contar os ACKs.")


# ------------------------------------------------------------------------------------------------------------ #
