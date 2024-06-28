'''
Autora: Samara dos Santos Ferreira
Última modificação: 2024-06-22
'''

# Importar as bibliotecas necessárias
import __init__
from time import sleep
#from api import API
from os import system, name
from consortium.api import API


# Limpar o terminal antes de iniciar
def clear():
    # no windows e no linux
    system('cls' if name == 'nt' else 'clear')


def active_bank(ip, port):
    try:
        clear()
        print(f"Api do banco financeiro rodando no IP {ip} e na porta {port}!")
        API.app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
    except KeyboardInterrupt:
        print("Api encerrada!")
        sleep(0.5)
        exit(0)