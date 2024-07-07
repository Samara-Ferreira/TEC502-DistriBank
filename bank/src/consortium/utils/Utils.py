'''
Descrição: Arquivo que contém as funções auxiliares do projeto.
'''


# Função para gerar o número da agência e da conta
def generate_agency_account(cnpj, len_clients):
    cnpj_aux = cnpj.replace(".", "")
    cnpj_aux = cnpj_aux[-3:]
    agency = "0" + cnpj_aux
    account = agency + f"-{len_clients + 1}"
    return agency, account


# Função para gerar a chave aleatória
def generate_random_key():
    from random import choices
    return ''.join(choices("0123456789abcdefghijklmnopqrstuvwxyz", k=32))


# Função para gerar a resposta de erro
def make_response(e):
    from flask import make_response
    import json
    response = make_response(json.dumps({"error": str(e)}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


# Função para imprimir texto colorido
def print_color(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'pink': '\033[95m',
        'blue': '\033[34m',
        'reset': '\033[0m'
    }

    color_code = colors.get(color, colors['reset'])
    reset_code = colors['reset']
    return f"{color_code}{text}{reset_code}"
