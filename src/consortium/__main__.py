'''
Autora: Samara dos Santos Ferreira
Última modificação: 2024-06-29
Descrição: este código refere-se ao principal do projeto, onde é iniciado o servidor da api do banco financeiro.
'''

# Importar as bibliotecas necessárias
import __init__
#import consortium.api.API as API

from api import API
from time import sleep
from os import system, name


# Limpar o terminal antes de iniciar
def clear():
    # no windows e no linux
    system('cls' if name == 'nt' else 'clear')


# Iniciar o servidor da api
if __name__ == "__main__":
    try:
        clear()
        cnpj = API.get_cnpj()
        print(f"API do banco financeiro rodando na porta {API.PORT}, com IP {cnpj}")
        API.app.run(host="0.0.0.0", port=API.PORT, debug=False, threaded=True)

    except KeyboardInterrupt as e:
        print("api encerrada!")
        sleep(0.5)
        exit(0)
