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
host4 = "172.16.103.6"

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
async def main(num, pack):
    # Criação das contas
    if num == 1:
        urls = [
            f"http://{host1}:{port1}/Thiago/08300000000/thiago03/thiago123/100.0/create_physical_particular",

            f"http://{host2}:{port2}/Silvio/08100000000/silvio11/silvio123/200.0/create_physical_joint",
            f"http://{host2}:{port2}/08100000000/João/08500000000/joao11/joao123/create_joint_complementary",
            f"http://{host2}:{port2}/08100000000/Thiago/08300000000/thiago03/thiago123/create_joint_complementary",

            f"http://{host3}:{port3}/Empresa/01400000000000/Silvio/silvio11/08100000000/silvio123/300.0/create_juridic_account",
            f"http://{host3}:{port3}/01400000000000/Thiago/thiago03/08300000000/thiago123/create_juridic_employee",

            f"http://{host4}:{port4}/Silvio/08100000000/silvio11/silvio123/100.0/create_physical_particular"
        ]

    # Criação das chaves PIX
    elif num == 2:
        urls = [
            f"http://{host1}:{port1}/08300000000/physical/cpf_cnpj/08300000000/create_pix_key",

            f"http://{host2}:{port2}/08100000000/physical_joint/random/null/create_pix_key",
            f"http://{host2}:{port2}/08500000000/physical_joint/email/joao@uefs/create_pix_key",

            f"http://{host3}:{port3}/08100000000/juridic/phone/75999999999/create_pix_key",
            f"http://{host3}:{port3}/08300000000/juridic/email/thiago@uefs/create_pix_key",

            f"http://{host4}:{port4}/08100000000/physical/email/silvio@uefs/create_pix_key"
        ]

    # Realização de depósitos
    elif num == 3:
        urls = [
            f"http://{host1}:{port1}/{host1}/{port1}/08300000000/physical/50.0/create_deposit",

            f"http://{host2}:{port2}/{host2}/{port2}/08100000000/physical_joint/50.0/create_deposit",
            f"http://{host2}:{port2}/{host2}/{port2}/08500000000/physical_joint/50.0/create_deposit",

            f"http://{host3}:{port3}/{host3}/{port3}/08100000000/juridic/50.0/create_deposit",
            f"http://{host3}:{port3}/{host3}/{port3}/08300000000/juridic/50.0/create_deposit",

            f"http://{host4}:{port4}/{host4}/{port4}/08100000000/physical/50.0/create_deposit"
        ]

    # Realização de saques
    elif num == 4:
        urls = [
            f"http://{host1}:{port1}/{host1}/{port1}/08300000000/physical/50.0/create_withdraw",

            f"http://{host2}:{port2}/{host2}/{port2}/08100000000/physical_joint/50.0/create_withdraw",
            f"http://{host2}:{port2}/{host2}/{port2}/08500000000/physical_joint/50.0/create_withdraw",

            f"http://{host3}:{port3}/{host3}/{port3}/08100000000/juridic/50.0/create_withdraw",
            f"http://{host3}:{port3}/{host3}/{port3}/08300000000/juridic/50.0/create_withdraw",

            f"http://{host4}:{port4}/{host4}/{port4}/08100000000/physical/50.0/create_withdraw"
        ]

    # Realização de transferências
    elif num == 5:
        urls = [
            f"http://{host1}:{port1}/{pack}/create_transfer",
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
    # Visualização de todos os clientes de cada banco
    if num == 1:
        print("=====================================")
        print("  Verificar clientes cadastrados")
        print("=====================================")
        response = requests.get(f"http://{host1}:{port1}/get_clients")
        print("Clients do Banco 1: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/get_clients")
        print("Clients do Banco 2: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/get_clients")
        print("Clients do Banco 3: ", print_correctly(response))
        response = requests.get(f"http://{host4}:{port4}/get_clients")
        print("Clients do Banco 4: ", print_correctly(response))

    # Visualização das chaves PIX de cada cliente
    elif num == 2:
        print("=====================================")
        print("       Verificar chaves PIX")
        print("=====================================")
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

    elif num == 3:
        print("=====================================")
        print("        Verificar extratos")
        print("=====================================")
        response = requests.get(f"http://{host1}:{port1}/08300000000/physical/get_balance")
        print("Saldo do cliente do B1: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/08100000000/physical_joint/get_balance")
        print("Saldo do cliente do B2: ", print_correctly(response))
        response = requests.get(f"http://{host2}:{port2}/08500000000/physical_joint/get_balance")
        print("Saldo do cliente do B2: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/08100000000/juridic/get_balance")
        print("Saldo do cliente do B3: ", print_correctly(response))
        response = requests.get(f"http://{host3}:{port3}/08300000000/juridic/get_balance")
        print("Saldo do cliente do B3: ", print_correctly(response))
        response = requests.get(f"http://{host4}:{port4}/08100000000/physical/get_balance")
        print("Saldo do cliente do B4: ", print_correctly(response))

    else:
        print("Operação inválida")


print("=====================================")
print("      Teste 1: Criar contas")
print("=====================================")
asyncio.run(main(1, None))
print_operations(1)

# print("=====================================")
# print("    Teste 2: Criar chaves PIX")
# print("=====================================")
# asyncio.run(main(2, None))
# print_operations(2)

# print("=====================================")
# print("   Teste 3: Realizar Depósitos")
# print("=====================================")
# asyncio.run(main(3, None))
# print_operations(3)       # O saldo de todos fica com 50.0 a mais (normal)
# B1 = 150.0
# B2 = 300.0
# B3 = 400.0
# B4 = 150.0

# print("=====================================")
# print("   Teste 4: Realizar Saques")
# print("=====================================")
# asyncio.run(main(4, None))
# print_operations(3)     # O saldo de todos fica com 50.0 a menos (normal)

# print("=====================================")
# print("  Teste 5: Realizar Transferências")
# print("=====================================")

# Pacote de transferência: B1, B2 e B3 -> B4
pack1 = [
    # Transferência do B1 para o B4
    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    },

    # Transferência do B2 para B4
    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host2, "port_send": port2, "cpf_send": "08300000000",
        "type_send": "physical_joint", "value": 10.0, "operation": "transfer"
    },

    # Transferência do B3 para B4
    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host3, "port_send": port3, "cpf_send": "08300000000",
        "type_send": "juridic", "value": 10.0, "operation": "transfer"
    }
]
# asyncio.run(main(5, pack1))
# print_operations(3)     # O saldo do B4 fica com 30.0 a mais e o saldo dos outros bancos com 10.0 a menos
# B1 = 90.0
# B2 = 190.0
# B3 = 290.0
# B4 = 130.0

# Pacote de transferência: B1 -> B2, B1 -> B3, B2 -> B4
pack2 = [
    {
        "host_recp": host2, "port_recp": port2, "cpf_recp": "08500000000",
        "type_recp": "physical_joint", "key_recp": "joao@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    },

    {
        "host_recp": host3, "port_recp": port3, "cpf_recp": "08300000000",
        "type_recp": "juridic", "key_recp": "thiago@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    },

    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host2, "port_send": port2, "cpf_send": "08300000000",
        "type_send": "physical_joint", "value": 10.0, "operation": "transfer"
    }
]
# asyncio.run(main(5, pack2))
# print_operations(3)     # O saldo do B3 e B4 fica com 10.0 a mais e o saldo do B1 com 20.0 a menos
# B1 = 70.0
# B2 = 190.0
# B3 = 300.0
# B4 = 140.0

# Pacote de transferência: B1, B2 e B3 -> B4 (saldo de B2 insuficiente)
pack3 = [
    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    },

    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host2, "port_send": port2, "cpf_send": "08300000000",
        "type_send": "physical_joint", "value": 500.0, "operation": "transfer"
    },

    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host3, "port_send": port3, "cpf_send": "08300000000",
        "type_send": "juridic", "value": 10.0, "operation": "transfer"
    }
]
# asyncio.run(main(5, pack3))
# print_operations(3)    # Nenhuma transferência é realizada


# Pacote de transferência: B1, B2 e B3 -> B4 (B4 não existe)
pack4 = [
    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    },

    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08100000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host2, "port_send": port2, "cpf_send": "08300000000",
        "type_send": "physical_joint", "value": 10.0, "operation": "transfer"
    },

    {
        "host_recp": host4, "port_recp": port4, "cpf_recp": "08900000000",
        "type_recp": "physical", "key_recp": "silvio@uefs",
        "host_send": host3, "port_send": port3, "cpf_send": "08300000000",
        "type_send": "juridic", "value": 10.0, "operation": "transfer"
    }
]
# asyncio.run(main(5, pack4))
# print_operations(3)    # Nenhuma transferência é realizada

# Teste para confiabilidade: transferência B1 -> B2
pack5 = [
    {
        "host_recp": host2, "port_recp": port2, "cpf_recp": "08500000000",
        "type_recp": "physical_joint", "key_recp": "joao@uefs",
        "host_send": host1, "port_send": port1, "cpf_send": "08300000000",
        "type_send": "physical", "value": 10.0, "operation": "transfer"
    }
]
# asyncio.run(main(5, pack5))     # Nenhuma transferência é realizada

# Só depois da conexão retornar
# print_operations(3)    # saldos atualizados B1 -10.0 e B2 + 10.0
