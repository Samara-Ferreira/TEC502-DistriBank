'''
Arquivo que contém os testes para criação de contas físicas particulares, conjuntas e jurídicas, do administrador e
de outros complementares.
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


async def create_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            return await response.json()


async def main(num):
    if num == 1:
        urls = [
            # f"http://{host1}:{port1}/maria/08500000000/maria11/maria123/100.0/create_physical_particular",
            # f"http://{host2}:{port2}/jose/08600000000/jose11/jose123/200.0/create_physical_joint",
            # f"http://{host2}:{port2}/08600000000/maria/08500000000/maria11/maria123/create_joint_complementary",
            # f"http://{host3}:{port3}/empresa/01400000000000/paula/paula11/08700000000/paula123/300.0/create_juridic_account",
            # f"http://{host4}:{port3}/01400000000000/paulo/paulo11/08800000000/paulo123/create_juridic_employee",
            # f"http://{host4}:{port4}/lucas/08900000000/lucas11/lucas123/500.0/create_physical_particular"

            f"http://{host_local}:{port1}/maria/08500000000/maria11/maria123/100.0/create_physical_particular",
            f"http://{host_local}:{port2}/jose/08600000000/jose11/jose123/200.0/create_physical_joint",
            f"http://{host_local}:{port2}/08600000000/maria/08500000000/maria11/maria123/create_joint_complementary",
            f"http://{host_local}:{port3}/empresa/01400000000000/paula/paula11/08700000000/paula123/300.0/create_juridic_account",
            f"http://{host_local}:{port3}/01400000000000/paulo/paulo11/08800000000/paulo123/create_juridic_employee",
            f"http://{host_local}:{port4}/lucas/08900000000/lucas11/lucas123/500.0/create_physical_particular"
        ]

    elif num == 2:
        urls = [
            # f"http://{host1}:{port1}/08500000000/physical/cpf_cnpj/08500000000/create_pix_key",
            # f"http://{host2}:{port2}/08600000000/physical_joint/random/null/create_pix_key",
            # f"http://{host2}:{port2}/08500000000/physical_joint/email/maria@/create_pix_key",
            # f"http://{host3}:{port3}/08700000000/juridic/phone/75999999999/create_pix_key",
            # f"http://{host3}:{port3}/08800000000/juridic/email/paulo@/create_pix_key",
            # f"http://{host4}:{port4}/08900000000/physical/email/lucas@/create_pix_key"
            
            f"http://{host_local}:{port1}/08500000000/physical/cpf_cnpj/08500000000/create_pix_key",
            f"http://{host_local}:{port2}/08600000000/physical_joint/random/null/create_pix_key",
            f"http://{host_local}:{port2}/08500000000/physical_joint/email/maria@/create_pix_key",
            f"http://{host_local}:{port3}/08700000000/juridic/phone/75999999999/create_pix_key",
            f"http://{host_local}:{port3}/08800000000/juridic/email/paulo@/create_pix_key",
            f"http://{host_local}:{port4}/08900000000/physical/email/lucas@/create_pix_key"
        ]

    else:
        urls = []

    tasks = [create_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(json.dumps(result, indent=4, ensure_ascii=False))


def print_get_clients():
    # response = requests.get(f"http://{host1}:{port1}/get_clients")
    # print("Banco 1: ", response.json())
    # response = requests.get(f"http://{host2}:{port2}/get_clients")
    # print("Banco 2: ", response.json())
    # response = requests.get(f"http://{host3}:{port3}/get_clients")
    # print("Banco 3: ", response.json())
    # response = requests.get(f"http://{host4}:{port4}/get_clients")
    # print("Banco 4: ", response.json())

    response = requests.get(f"http://{host_local}:{port1}/get_clients")
    print("Banco 1: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port2}/get_clients")
    print("Banco 2: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port3}/get_clients")
    print("Banco 3: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port4}/get_clients")
    print("Banco 4: ", print_correctly(response))


def print_get_keys(cpf, type):
    response = requests.get(f"http://{host_local}:{port1}/{cpf}/{type}/get_keys")
    return print_correctly(response)


def print_correctly(response):
    content = response.json()
    return json.dumps(content, indent=4, ensure_ascii=False)


print("\n\t", "-"*60)
print("\t\t\tCriação de contas")
print("\t", "-"*60)

asyncio.run(main(1))

print("\n\t--- Clientes dos bancos ")
print_get_clients()


print("\n\t", "-"*60)
print("\t\t\tCriação das chaves pix")
print("\t", "-"*60)

asyncio.run(main(2))

print("\n\t--- Chaves pix dos clientes")
response = requests.get(f"http://{host_local}:{port1}/08500000000/physical/get_keys")
response = print_correctly(response)
print("Cliente 1: ", response)

response = requests.get(f"http://{host_local}:{port2}/08600000000/physical_joint/get_keys")
response = print_correctly(response)
print("Cliente 2: ", response)

response = requests.get(f"http://{host_local}:{port2}/08500000000/physical_joint/get_keys")
response = print_correctly(response)
print("Cliente 3: ", response)

response = requests.get(f"http://{host_local}:{port3}/08700000000/juridic/get_keys")
response = print_correctly(response)
print("Cliente 4: ", response)

response = requests.get(f"http://{host_local}:{port3}/08800000000/juridic/get_keys")
response = print_correctly(response)
print("Cliente 5: ", response)

response = requests.get(f"http://{host_local}:{port4}/08900000000/physical/get_keys")
response = print_correctly(response)
print("Cliente 6: ", response)

print("\n\t--- Tentar criar a chave pix com chave existente, só que em outro cliente")
response = requests.post(f"http://{host_local}:{port1}/maria@/physical/email/08500000000/create_pix_key")    # chave B2
print("Cliente 1: ", print_correctly(response))

print("\tRetorno")
response = requests.get(f"http://{host_local}:{port1}/08500000000/physical/get_keys")
response = print_correctly(response)
print("Cliente 1: ", response)

print("\n\t", "-"*60)
