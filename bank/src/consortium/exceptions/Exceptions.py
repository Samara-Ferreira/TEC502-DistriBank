'''
Descrição: Arquivo que contém as exceções personalizadas.
'''


class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Exceção: {self.message}"


class ClientNotFound(MyException):
    def __init__(self):
        super().__init__("Cliente não encontrado.")


class InvalidPassword(MyException):
    def __init__(self):
        super().__init__("Senha inválida.")


class ClientAlreadyExists(MyException):
    def __init__(self):
        super().__init__("Cliente já existe.")


class KeyAlreadyExists(MyException):
    def __init__(self):
        super().__init__("Chave já existe.")


class InvalidKey(MyException):
    def __init__(self):
        super().__init__("Chave inválida.")


class KeyNotFound(MyException):
    def __init__(self):
        super().__init__("Chave não encontrada.")


class QueueIsEmpty(MyException):
    def __init__(self):
        super().__init__("A fila está vazia.")


class InsufficientBalance(MyException):
    def __init__(self):
        super().__init__("Saldo insuficiente.")


class BankIsInactive(MyException):
    def __init__(self):
        super().__init__("Banco inativo.")

