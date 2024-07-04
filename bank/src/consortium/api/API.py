'''
Descrição: este código é referente ao banco financeiro, onde são definidas as funções principais do banco, como criar
conta, deletar conta, criar chave pix, depositar e sacar dinheiro, realizar transações, entre outras.
'''

# Importar as bibliotecas necessárias
import __init__
import Bank
import utils.Utils as Utils
import exceptions.Exceptions as Exceptions
import api.FloatConverter as FloatConverter

from os import getenv
from flask import Flask, jsonify, request


# Definir o tipo e a porta do banco
# PORT = 5551
PORT = getenv("PORT")

# Instanciar a classe do banco
bank = Bank.Bank(int(PORT))

# Iniciar a API
app = Flask(__name__)
app.url_map.converters['float'] = FloatConverter.FloatConverter


# Função para obter o CNPJ do banco
def get_cnpj():
    return bank.cnpj


def get_bank():
    return bank


# Rota para fazer login na conta
@app.route("/<string:type>/<string:user>/<string:password>/login", methods=["POST"])
def login(type, user, password):
    try:
        return jsonify(bank.login(type, user, password))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    except Exceptions.InvalidPassword:
        return jsonify({"error": "Senha incorreta!"}), 401


# Rota para deslogar da conta
@app.route("/<string:user>/logout", methods=["POST"])
def logout(user):
    try:
        return jsonify(bank.logout(user))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404


# Rota para criar uma conta física particular
@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_particular",
           methods=["POST"])
def create_physical_particular(name, cpf, user, password, balance):
    try:
        return jsonify(bank.create_physical_particular(name, cpf, user, password, balance))
    except Exceptions.ClientAlreadyExists:
        return jsonify({"error": "Cliente já existe!"}), 409


# Rota para criar uma conta física conjunta
@app.route("/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>"
           "/create_physical_joint", methods=["POST"])
def create_physical_joint(name, cpf, user, password, balance):
    try:
        return jsonify(bank.create_physical_joint(name, cpf, user, password, balance))
    except Exceptions.ClientAlreadyExists:
        return jsonify({"error": "Cliente já existe!"}), 409


# Rota para criar uma conta física conjunta complementar
@app.route("/<string:cpf_holder>/<string:name>/<string:cpf>/<string:user>/<string:password>"
           "/create_joint_complementary",
           methods=["POST"])
def create_joint_complementary(cpf_holder, name, cpf, user, password):
    try:
        return jsonify(bank.create_joint_complementary(cpf_holder, name, cpf, user, password))
    except Exceptions.ClientAlreadyExists:
        return jsonify({"error": "Cliente já existe!"}), 409
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente titular não encontrado!"}), 404


# Rota para criar uma conta jurídica
@app.route("/<string:name_company>/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>"
           "/<float:balance>/create_juridic_account", methods=["POST"])
def create_juridic_account(name_company, cnpj, name, user, cpf, password, balance):
    try:
        return jsonify(bank.create_juridic_account(name_company, cnpj, name, user, cpf, password, balance))
    except Exceptions.ClientAlreadyExists:
        return jsonify({"error": "Cliente já existe!"}), 409


# Rota para criar uma conta jurídica para funcionário
@app.route("/<string:cnpj>/<string:name>/<string:user>/<string:cpf>/<string:password>"
           "/create_juridic_employee", methods=["POST"])
def create_juridic_employee(cnpj, name, user, cpf, password):
    try:
        return jsonify(bank.create_juridic_employee(cnpj, name, user, cpf, password))
    except Exceptions.ClientAlreadyExists:
        return jsonify({"error": "Cliente já existe!"}), 409
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente titular não encontrado!"}), 404


# Rota para obter todos os clientes do banco
@app.route("/get_clients", methods=["GET"])
def get_clients():
    try:
        return jsonify(bank.get_clients())
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Não há clientes cadastrados!"}), 404

# ------------------------------ Account Management ------------------------------


# Rota para criação de uma chave pix
@app.route("/<string:cpf>/<string:type_account>/<string:type_key>/<string:value>/create_pix_key",
           methods=["POST"])
def create_pix_key(cpf, type_account, type_key, value):
    try:
        return jsonify(bank.create_pix_key(cpf, type_account, type_key, value))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    except Exceptions.KeyAlreadyExists:
        return jsonify({"error": "Chave já existe!"}), 409
    except Exceptions.InvalidKey:
        return jsonify({"error": "Chave inválida!"}), 400
    except Exceptions.BankIsInactive:
        return jsonify({"error": "Um dos banco está inativo! Tente novamente mais tarde."}), 400


# Rota para obter as chaves pix de um cliente
@app.route("/<string:cpf>/<string:type>/get_keys", methods=["GET"])
def get_keys(cpf, type):
    try:
        return jsonify(bank.get_keys(cpf, type))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404


# Rota para obter o saldo de uma conta
@app.route("/<string:cpf>/<string:type>/get_balance", methods=["GET"])
def get_balance(cpf, type):
    try:
        return jsonify(bank.get_balance(cpf, type))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404


# Rota para obter o extrato bancário
@app.route("/get_bank_statement", methods=["GET"])
def get_bank_statement():
    try:
        return jsonify(bank.get_queue_executed())
    except Exceptions.QueueIsEmpty:
        return jsonify({"error": "Fila vazia!"}), 404


# Rota para criar um depósito
@app.route("/<string:host>/<string:port>/<string:cpf>/<string:type>/<float:value>/create_deposit",
           methods=["POST"])
def create_deposit(host, port, cpf, type, value):
    return jsonify(bank.create_deposit(host, port, cpf, type, value))


# Rota para criar um saque
@app.route("/<string:host>/<string:port>/<string:cpf>/<string:type>/<float:value>/create_withdraw",
           methods=["POST"])
def create_withdraw(host, port, cpf, type, value):
    return jsonify(bank.create_withdraw(host, port, cpf, type, value))


# Rota para realizar um depósito
@app.route("/<string:cpf_cnpj>/<string:type>/<string:key>/<float:value>/deposit",
           methods=["POST"])
def deposit(cpf_cnpj, type, key, value):
    try:
        return jsonify(bank.deposit(cpf_cnpj, type, key, value))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    except Exceptions.KeyNotFound:
        return jsonify({"error": "Chave não encontrada!"}), 404


# Rota para realizar um depósito interno
@app.route("/<string:cpf>/<string:type>/<float:value>/in_deposit", methods=["POST"])
def in_deposit(cpf, type, value):
    try:
        return jsonify(bank.in_deposit(cpf, type, value))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404


# Rota para realizar um saque
@app.route("/<string:cpf_cnpj>/<string:type>/<string:key>/<float:value>/withdraw",
           methods=["POST"])
def withdraw(cpf_cnpj, type, key, value):
    try:
        return jsonify(bank.withdraw(cpf_cnpj, type, key, value))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    except Exceptions.KeyNotFound:
        return jsonify({"error": "Chave não encontrada!"}), 404
    except Exceptions.InsufficientBalance:
        return jsonify({"error": "Saldo insuficiente!"}), 400


# Rota para realizar um saque interno
@app.route("/<string:cpf>/<string:type>/<float:value>/in_withdraw", methods=["POST"])
def in_withdraw(cpf, type, value):
    try:
        return jsonify(bank.in_withdraw(cpf, type, value))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    except Exceptions.InsufficientBalance:
        return jsonify({"error": "Saldo insuficiente!"}), 400


# Rota para criar uma transferência
@app.route("/<string:operations>/create_transfer", methods=["POST"])
def create_transfer(operations):
    return jsonify(bank.create_transfer(operations))

# ------------------------------ Operations ------------------------------


# Rota para deletar a primeira operação da fila de prioridade
@app.route("/delete_first_operation", methods=["GET"])
def delete_first_operations():
    return jsonify(bank.delete_first_operation())


# Rota para adicionar a primeira operação da fila de prioridade
@app.route("/<string:operation>/add_first_operation", methods=["GET"])
def add_first_operation(operation):
    return jsonify(bank.add_first_operation(operation))


# Rota para obter a primeira operação da fila
@app.route("/get_first_operation", methods=["GET"])
def get_first_operation():
    return jsonify(bank.get_first_operation())


# Rota para receber uma nova operação
@app.route("/<string:operation>/receive_new_operation", methods=["GET"])
def receive_new_operation(operation):
    return jsonify(bank.receive_new_operation(operation))


# Rota para receber um ack
@app.route("/<string:ack>/receive_ack", methods=["GET"])
def receive_ack(ack):
    return jsonify(bank.receive_ack(ack))


# Rota para obter os acks
@app.route("/get_acks", methods=["GET"])
def get_acks():
    return jsonify(bank.get_acks())


# Rota para verificar se o cliente existe
@app.route("/<string:cpf>/<string:type>/check_client", methods=["GET"])
def check_client(cpf, type):
    try:
        return jsonify(bank.check_client(cpf, type))
    except Exceptions.ClientNotFound:
        return jsonify({"error": "Cliente não encontrado!"}), 404


# Rota para limpar a fila de prioridade
@app.route("/delete_queue", methods=["GET"])
def delete_queue():
    return jsonify(bank.delete_queue())

