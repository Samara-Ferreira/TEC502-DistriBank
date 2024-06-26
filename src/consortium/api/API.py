'''
Descrição: Arquivo referente ao banco financeiro, onde são definidas as funções principais do banco,
como criar conta, deletar conta, criar chave pix, depositar e sacar dinheiro, realizar transações, entre outras.
'''

# Importar as bibliotecas necessárias
import __init__
import Bank
import FloatConverter
import utils.Utils as Utils
import exceptions.Exceptions as Exceptions

from os import getenv
from flask import Flask, jsonify

# Definir o tipo e a porta do banco
TYPE = "1"
PORT = 5551
#TYPE = getenv("TYPE")
#PORT = getenv("PORT")

# Iniciar o banco
bank = Bank.Bank(TYPE, PORT)
app = Flask(__name__)
app.url_map.converters['float'] = FloatConverter.FloatConverter


def get_cnpj():
    return bank.cnpj


# ------------------------------------ Rotas para as operações ------------------------------------ #

# Rota para adicionar uma nova operação
@app.route("/<string:operation>/add_new_operation", methods=["GET"])
def add_element_in(operation):
    try:
        return jsonify(bank.operations.add_new_operation(operation))
    except Exceptions as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para adicionar a primeira operação
@app.route("/<string:operation>/add_first_operation", methods=["GET"])
def add_first_operation(operation):
    return jsonify(bank.operations.add_first_operation(operation))


# Rota para deletar a primeira operação
@app.route("/delete_first_operation", methods=["GET"])
def delete_first_operation():
    try:
        return jsonify(bank.delete_first_operation())
    except Exceptions.ErrorDeletingOperation as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para obter a primeira operação
@app.route("/get_first_operation", methods=["GET"])
def get_first_operation():
    try:
        return jsonify(bank.get_first_operation())
    except Exceptions as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para enviar uma nova operação
@app.route("/<string:operation>/receive_new_operation", methods=["GET"])
def receive_new_operation(operation):
    try:
        return jsonify(bank.receive_new_operation(operation))
    except Exceptions.ErrorSendingOperation as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para receber um ACK
@app.route("/<string:ack>/receive_ack", methods=["GET"])
def receive_ack(ack):
    try:
        return jsonify(bank.receive_ack(ack))
    except Exceptions.ErrorSendingACK as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para obter a lista de ACKs
@app.route("/return_ack", methods=["GET"])
def return_ack():
    return jsonify(bank.return_acks())


# Rota para obter a fila de prioridade
@app.route("/return_queues", methods=["GET"])
def return_queues():
    return jsonify(bank.return_queues())


# Rota para obter a fila das operações executadas
@app.route("/return_executed", methods=["GET"])
def return_executed():
    return jsonify(bank.return_executed())


# ------------------------------------ Rotas para a criação de contas ------------------------------------ #

@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_particular",
           methods=["GET"])
def create_physical_particular(name, cpf, user, password, balance):
    try:
        return bank.create_physical_particular(name, cpf, user, password, balance)
    except Exceptions.ClientAlreadyExists as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCPF as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidBalance as e:
        response = Utils.make_response(e)
        return response, 400


@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_joint",
           methods=["GET"])
def create_physical_joint(name, cpf, user, password, balance):
    try:
        return bank.create_physical_joint(name, cpf, user, password, balance)
    except Exceptions.ClientAlreadyExists as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCPF as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidBalance as e:
        response = Utils.make_response(e)
        return response, 400


@app.route("/<string:cpf_holder>/<string:name>/<string:cpf>/<string:user>/<string:password>/create_joint_complementary",
           methods=["GET"])
def create_joint_complementary(cpf_holder, name, cpf, user, password):
    try:
        return bank.create_joint_complementary(cpf_holder, name, cpf, user, password)
    except Exceptions.ClientAlreadyExists as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCPF as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400


@app.route("/<string:name_company>/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>/<float:balance>/"
           "create_juridic_account", methods=["GET"])
def create_juridic_account(name_company, cnpj, name, user, cpf, password, balance):
    try:
        return bank.create_juridic_account(name_company, cnpj, name, user, cpf, password, balance)
    except Exceptions.ClientAlreadyExists as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCNPJ as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidBalance as e:
        response = Utils.make_response(e)
        return response, 400


@app.route("/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>/create_juridic_employee",
           methods=["GET"])
def create_juridic_employee(cnpj, name, user, cpf, password):
    try:
        return bank.create_juridic_employee(cnpj, name, user, cpf, password)
    except Exceptions.ClientAlreadyExists as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCPF as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para obter a lista de clientes
@app.route("/return_clients", methods=["GET"])
def return_clients():
    return jsonify(bank.return_clients())


# ------------------------------------ Rotas para as transações ------------------------------------ #

# Rota para criação de uma chave pix
@app.route("/<string:cpf_cnpj>/<string:type_account>/<string:type_pix_key>/<string:pix_key>/create_pix_key",
           methods=["GET"])
def create_pix_key(cpf_cnpj, type_account, type_pix_key, pix_key):
    try:
        return bank.create_pix_key(cpf_cnpj, type_account, type_pix_key, pix_key)
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCPF as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidCNPJ as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidEmail as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPhone as e:
        response = Utils.make_response(e)
        return response, 400

# Rota para retornar as chaves pix cadastradas
@app.route("/return_keys", methods=["GET"])
def return_keys():
    return jsonify(bank.return_keys())
