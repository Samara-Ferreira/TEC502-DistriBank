'''
    Descrição: Este arquivo contém os testes unitários para a aplicação, usados para a apresentação
    do trabalho.
'''

import json
import asyncio
import aiohttp
import requests
from os import system, name


system('cls' if name == 'nt' else 'clear')

host1 = "172.16.103.1"
host2 = "172.16.103.2"
host3 = "172.16.103.4"
host4 = "172.16.103.5"

host_local = "172.22.208.1"

port1 = 5551
port2 = 5552
port3 = 5553
port4 = 5554


# Função para criar uma requisição
async def create_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            return await response.json()

# Função para realizar as requisições
async def main(num):
    if num == 1:
        urls = [
            f"http://{host1}:{port1}/Thiago/08300000000/thiago03/thiago123/100.0/create_physical_particular",
            f"http://{host2}:{port2}/Silvio/08100000000/silvio11/silvio123/200.0/create_physical_joint",
            f"http://{host2}:{port2}/08100000000/João/08500000000/joao11/joao123/create_joint_complementary",
            f"http://{host3}:{port3}/Empresa/01400000000000/Silvio/silvio11/08100000000/silvio123/300.0/create_juridic_account",
            f"http://{host3}:{port3}/01400000000000/Thiago/thiago03/08300000000/thiago123/create_juridic_employee",
            f"http://{host4}:{port4}/Silvio/08100000000/silvio11/silvio123/100.0/create_physical_particular"
        ]

    elif num == 2:
        urls = [
            f"http://{host1}:{port1}/08300000000/physical/cpf_cnpj/08300000000/create_pix_key",
            f"http://{host2}:{port2}/08100000000/physical_joint/random/null/create_pix_key",
            f"http://{host2}:{port2}/08500000000/physical_joint/email/joao@/create_pix_key",
            f"http://{host3}:{port3}/08100000000/juridic/phone/75999999999/create_pix_key",
            f"http://{host3}:{port3}/08300000000/juridic/email/thiago@uefs/create_pix_key",
            f"http://{host4}:{port4}/08100000000/physical/email/silviu@uefs/create_pix_key"
        ]

    elif num == 3:
        urls = [
            f"http://{host1}:{port1}/{host1}/{port1}/08300000000/physical/50.0/create_deposit",
            f"http://{host2}:{port2}/{host2}/{port2}/08100000000/physical_joint/50.0/create_deposit",
            f"http://{host2}:{port2}/{host2}/{port2}/08500000000/physical_joint/50.0/create_deposit",
            f"http://{host3}:{port3}/{host3}/{port3}/08100000000/juridic/50.0/create_deposit",
            f"http://{host3}:{port3}/{host3}/{port3}/08300000000/juridic/50.0/create_deposit",
            f"http://{host4}:{port4}/{host4}/{port4}/08100000000/physical/50.0/create_deposit"
        ]

    else:
        urls = []

    tasks = [create_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(json.dumps(result, indent=4, ensure_ascii=False))


# Função para imprimir a resposta corretamente
def print_correctly(response):
    content = response.json()
    return json.dumps(content, indent=4, ensure_ascii=False)


# Função para imprimir as operações
def print_operations(num):
    if num == 1:
        response = requests.get(f"http://{host1}:{port1}/get_clients")
        print("Clients do Banco 1: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/get_clients")
        print("Clients do Banco 2: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/get_clients")
        print("Clients do Banco 3: ", print_correctly(response))
        response = requests.get(f"http://{host4}:{port4}/get_clients")
        print("Clients do Banco 4: ", print_correctly(response))

    elif num == 2:
        response = requests.get(f"http://{host1}:{port1}/08300000000/physical/get_keys")
        print("Chaves PIX do cliente do B1: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/08100000000/physical_joint/get_keys")
        print("Chaves PIX do cliente do B2: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/08500000000/physical_joint/get_keys")
        print("Chaves PIX do cliente do B2: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/08100000000/juridic/get_keys")
        print("Chaves PIX do cliente do B3: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/08300000000/juridic/get_keys")
        print("Chaves PIX do cliente do B3: ", print_correctly(response))
        response = requests.get(f"http://{host4}:{port4}/08100000000/physical/get_keys")
        print("Chaves PIX do cliente do B4: ", print_correctly(response))

    else:
        print("Operação inválida")


print("=====================================")
print("      Teste 1: Criar contas")
print("=====================================")
asyncio.run(main(1))
print_operations(1)

print("=====================================")
print("    Teste 2: Criar chaves PIX")
print("=====================================")
asyncio.run(main(2))
print_operations(2)

print("=====================================")
print("    Teste 3: Realizar transações")
print("=====================================")
asyncio.run(main(3))
print_operations(3)

print("=====================================")
print("    Teste 4: Verificar extratos")

