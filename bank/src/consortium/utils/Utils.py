'''
Descrição: Arquivo que contém as funções auxiliares
'''


def generate_agency_account(cnpj, len_clients):
    cnpj_aux = cnpj.replace(".", "")
    cnpj_aux = cnpj_aux[-3:]
    agency = "0" + cnpj_aux
    account = agency + f"-{len_clients + 1}"
    return agency, account


def generate_random_key():
    from random import choices
    return ''.join(choices("0123456789abcdefghijklmnopqrstuvwxyz", k=32))


def make_response(e):
    from flask import make_response
    import json
    response = make_response(json.dumps({"error": str(e)}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response
