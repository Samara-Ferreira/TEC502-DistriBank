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
            f"http://{host_local}:{port1}/{host_local}/{port1}/08500000000/physical/50.0/create_deposit",
            f"http://{host_local}:{port2}/{host_local}/{port2}/08600000000/physical_joint/50.0/create_deposit",
            f"http://{host_local}:{port2}/{host_local}/{port2}/08500000000/physical_joint/50.0/create_deposit",
            f"http://{host_local}:{port3}/{host_local}/{port3}/08700000000/juridic/50.0/create_deposit",
            f"http://{host_local}:{port3}/{host_local}/{port3}/08800000000/juridic/50.0/create_deposit",
            f"http://{host_local}:{port4}/{host_local}/{port4}/08900000000/physical/50.0/create_deposit"
        ]

    elif num == 2:
        urls = [
            f"http://{host_local}:{port1}/{host_local}/{port1}/08500000000/physical/50.0/create_withdraw",
            f"http://{host_local}:{port2}/{host_local}/{port2}/08600000000/physical_joint/50.0/create_withdraw",
            f"http://{host_local}:{port2}/{host_local}/{port2}/08500000000/physical_joint/50.0/create_withdraw",
            f"http://{host_local}:{port3}/{host_local}/{port3}/08700000000/juridic/50.0/create_withdraw",
            f"http://{host_local}:{port3}/{host_local}/{port3}/08800000000/juridic/50.0/create_withdraw",
            f"http://{host_local}:{port4}/{host_local}/{port4}/08900000000/physical/50.0/create_withdraw"
        ]

    elif num == 3:
        urls = [
            f"http://{host_local}:{port1}/{pack1}/create_transfer",
            f"http://{host_local}:{port1}/{pack2}/create_transfer",
            f"http://{host_local}:{port2}/{pack3}/create_transfer",
            f"http://{host_local}:{port3}/{pack4}/create_transfer"
        ]

    else:
        urls = []

    tasks = [create_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(json.dumps(result, indent=4, ensure_ascii=False))


def print_correctly(response):
    content = response.json()
    return json.dumps(content, indent=4, ensure_ascii=False)


def print_operations_bank():
    response = requests.get(f"http://{host_local}:{port1}/get_bank_statement")
    print("Banco 1: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port2}/get_bank_statement")
    print("Banco 2: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port3}/get_bank_statement")
    print("Banco 3: ", print_correctly(response))
    response = requests.get(f"http://{host_local}:{port4}/get_bank_statement")
    print("Banco 4: ", print_correctly(response))


print("\n\t", "-" * 60)
print("\t\t\t\tOperações em todas as contas")
print("\t", "-" * 60)

# Depósito
# asyncio.run(main(1))

# Saque
# asyncio.run(main(2))

# Transferência

# conta 1 -> conta 2
pack1 = [{"host_recp": host_local, "port_recp": port2, "cpf_recp": "08600000000",
          "type_recp": "physical_joint", "key_recp": "tttec983olabd01auydz4l8n0ezgci45",
          "host_send": host_local, "port_send": port1, "cpf_send": "08500000000",
          "type_send": "physical", "value": 10.0, "operation": "transfer"}]

# conta 1 -> conta 3
pack2 = [{"host_recp": host_local, "port_recp": port2, "cpf_recp": "08500000000",
          "type_recp": "physical_joint", "key_recp": "maria@",
          "host_send": host_local, "port_send": port1, "cpf_send": "08500000000",
          "type_send": "physical", "value": 10.0, "operation": "transfer"}]

# conta 2 -> conta 4
pack3 = [{"host_recp": host_local, "port_recp": port3, "cpf_recp": "08700000000",
          "type_recp": "juridic", "key_recp": "75999999999",
          "host_send": host_local, "port_send": port2, "cpf_send": "08600000000",
          "type_send": "physical_joint", "value": 10.0, "operation": "transfer"}]

# conta 4 -> conta 5
pack4 = [{"host_recp": host_local, "port_recp": port4, "cpf_recp": "08900000000",
          "type_recp": "physical", "key_recp": "lucas@",
          "host_send": host_local, "port_send": port3, "cpf_send": "08800000000",
          "type_send": "juridic", "value": 10.0, "operation": "transfer"}]

asyncio.run(main(3))

# saldos finais
# Conta 1:  70.0
# Conta 2:  220.0
# Conta 3:  220.0
# Conta 4:  300.0
# Conta 5:  300.0
# Conta 6:  510.0

print("\n\t--- Operações dos bancos ")
print_operations_bank()

print("\n\t--- Saldos de cada conta ")
response = requests.get(f"http://{host_local}:{port1}/08500000000/physical/get_balance")
print("Conta 1: ", print_correctly(response))

response = requests.get(f"http://{host_local}:{port2}/08600000000/physical_joint/get_balance")
print("Conta 2: ", print_correctly(response))

response = requests.get(f"http://{host_local}:{port2}/08500000000/physical_joint/get_balance")
print("Conta 3: ", print_correctly(response))

response = requests.get(f"http://{host_local}:{port3}/08700000000/juridic/get_balance")
print("Conta 4: ", print_correctly(response))

response = requests.get(f"http://{host_local}:{port3}/08800000000/juridic/get_balance")
print("Conta 5: ", print_correctly(response))

response = requests.get(f"http://{host_local}:{port4}/08900000000/physical/get_balance")
print("Conta 6: ", print_correctly(response))

print("\n\t", "-"*60)





