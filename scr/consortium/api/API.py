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


# ------------------------------------ Novas Rotas ------------------------------------#

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
@app.route("/return_executed", methods=["GET"])
def return_executed():
    return jsonify(bank.return_executed())


# ------------------------------------------------------------------------------------------------------------ #
