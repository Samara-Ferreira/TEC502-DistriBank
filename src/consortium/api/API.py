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
from flask import Flask, jsonify, request

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
        return jsonify(bank.add_new_operation(operation))
    except Exceptions as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para adicionar a primeira operação
@app.route("/<string:operation>/add_first_operation", methods=["GET"])
def add_first_operation(operation):
    return jsonify(bank.add_first_operation(operation))


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
@app.route("/get_queue_executed", methods=["GET"])
def get_queue_executed():
    return jsonify(bank.get_queue_executed())


# ------------------------------------ Rotas para a criação de contas ------------------------------------ #

# Rota para fazer o login de um cliente
@app.route("/<string:user>/<string:password>/login", methods=["GET"])
def login(user, password):
    try:
        return jsonify(bank.login(user, password))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InvalidPassword as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para fazer o logout de um cliente
@app.route("/<string:user>/logout", methods=["GET"])
def logout(user):
    try:
        return jsonify(bank.logout(user))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para criar uma conta física particular
@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_particular",
           methods=["GET"])
def create_physical_particular(name, cpf, user, password, balance):
    try:
        return jsonify(bank.create_physical_particular(name, cpf, user, password, balance))
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


# Rota para criar uma conta física conjunta
@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_joint",
           methods=["GET"])
def create_physical_joint(name, cpf, user, password, balance):
    try:
        return jsonify(bank.create_physical_joint(name, cpf, user, password, balance))
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


# Rota para criar uma conta física complementar
@app.route("/<string:cpf_holder>/<string:name>/<string:cpf>/<string:user>/<string:password>/create_joint_complementary",
           methods=["GET"])
def create_joint_complementary(cpf_holder, name, cpf, user, password):
    try:
        return jsonify(bank.create_joint_complementary(cpf_holder, name, cpf, user, password))
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


# Rota para criar uma conta jurídica
@app.route("/<string:name_company>/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>/<float:balance>/"
           "create_juridic_account", methods=["GET"])
def create_juridic_account(name_company, cnpj, name, user, cpf, password, balance):
    try:
        return jsonify(bank.create_juridic_account(name_company, cnpj, name, user, cpf, password, balance))
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


# Rota para criar um funcionário de uma conta jurídica
@app.route("/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>/create_juridic_employee",
           methods=["GET"])
def create_juridic_employee(cnpj, name, user, cpf, password):
    try:
        return jsonify(bank.create_juridic_employee(cnpj, name, user, cpf, password))
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
@app.route("/get_accounts", methods=["GET"])
def get_all_accounts():
    return jsonify(bank.get_accounts())

# ------------------------------------ Rotas para as transações ------------------------------------ #


# Rota para criação de uma chave pix
@app.route("/<string:cpf>/<string:type>/<string:type_key>/<string:key>/create_pix_key",
           methods=["GET"])
def create_pix_key(cpf, type, type_key, key):
    try:
        return jsonify(bank.create_pix_key(cpf, type, type_key, key))
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


# Rota para obter uma chave pix de um cliente
@app.route("/<string:cpf>/get_keys", methods=["GET"])
def get_keys(cpf):
    try:
        return jsonify(bank.get_keys(cpf))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400

# Rota para retornar as chaves pix cadastradas
'''@app.route("/return_keys", methods=["GET"])
def return_keys():
    return jsonify(bank.return_keys())'''


# Rota para realizar um depósito
@app.route("/<string:cpf_cnpj>/<string:type_account>/<string:pix_key>/<float:value>/deposit", methods=["POST"])
def deposit(cpf_cnpj, type_account, pix_key, value):
    try:
        return jsonify(bank.deposit(cpf_cnpj, type_account, pix_key, value))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para realizar um saque
@app.route("/<string:cpf_cnpj>/<string:type_account>/<string:pix_key>/<float:value>/withdraw", methods=["POST"])
def withdraw(cpf_cnpj, type_account, pix_key, value):
    try:
        return jsonify(bank.withdraw(cpf_cnpj, type_account, pix_key, value))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InsufficientBalance as e:
        response = Utils.make_response(e)
        return response, 400


'''@app.route("/return_balance", methods=["GET"])
def return_balances():
    try:
        return jsonify(bank.return_balances())
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400'''


# Rota para retornar o saldo de uma conta
@app.route("/<string:cpf>/<string:type>/get_balance", methods=["GET"])
def get_balance(cpf, type):
    try:
        return jsonify(bank.get_balance(cpf, type))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400


# Rota para obter o saldo específico de um cliente


# Rota para verificar se uma conta existe em outro banco ou não
'''@app.route("/<string:cpf_cnpj>/<string:pix_key>/check_account", methods=["GET"])
def check_account(cpf_cnpj, pix_key):
    try:
        return jsonify(bank.check_account(cpf_cnpj, pix_key))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400'''


# Rota para criar um depósito
@app.route("/<int:port>/<string:cpf>/<string:type>/<string:key>/<float:value>/create_deposit",
           methods=["GET"])
def create_deposit(port, cpf, type, key, value):
    try:
        return jsonify(bank.create_deposit(port, cpf, type, key, value))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400


# Método para criar um saque
@app.route("/<int:port>/<string:cpf>/<string:type>/<string:key>/<float:value>/create_withdraw",
           methods=["GET"])
def create_withdraw(port, cpf, type, key, value):
    try:
        return jsonify(bank.create_withdraw(port, cpf, type, key, value))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InsufficientBalance as e:
        response = Utils.make_response(e)
        return response, 400


'''@app.route("/<string:port_recp>/<string:port_send>/<string:cpf_recp>/<string:cpf_send>/<string:type_recp>/"
           "<string:type_send>/<string:key>/<float:value>/<string:same>/create_transfer", methods=["GET"])
def create_transfer(port_recp, port_send, cpf_recp, cpf_send, type_recp, type_send, key, value, same):
    try:
        return bank.create_transaction(port_recp, port_send, cpf_recp, cpf_send, type_recp, type_send, key, value, same)
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InsufficientBalance as e:
        response = Utils.make_response(e)
        return response, 400'''


# crie uma rota para essa requisição: requests.post(f"http://{self.host}:{self.port}/create_transfer", json=self.queue_transfer)
@app.route("/<string:operations>/create_transfer", methods=["POST"])
def create_transfer(operations):
    try:
        return jsonify(bank.create_transfer(operations))
    except Exceptions.ClientNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.KeyNotFound as e:
        response = Utils.make_response(e)
        return response, 400
    except Exceptions.InsufficientBalance as e:
        response = Utils.make_response(e)
        return response, 400

