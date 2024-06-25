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


def get_agency_port(key_receiver, cnpj):
    port = key_receiver[:4]
    agency = key_receiver[6:7] + "." + key_receiver[7:8]
    cnpj_aux = cnpj[:len(cnpj) - 3] + agency
    return agency, port, cnpj_aux


def clear():
    from os import system, name
    # no windows e no linux
    system('cls' if name == 'nt' else 'clear')


def make_response(e):
    from flask import make_response
    import json
    response = make_response(json.dumps({"error": str(e)}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response
