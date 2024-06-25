'''
Descrição: Arquivo que contém as exceções personalizadas.
'''


class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Exceção: {self.message}"


# ------------------------------------ Novas Exceções ------------------------------------ #
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
