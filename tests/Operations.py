import requests
import asyncio # add no docker
import aiohttp # add no docker
from time import sleep
from os import system, name

system('cls' if name == 'nt' else 'clear')

host1 = "192.168.0.111"
host2 = "172.16.103.2"

port1 = 5551
port2 = 5552
port3 = 5553
port4 = 5554

# ------------------------------------------------------------------------------------------------------------ #

async def fazer_requisicao(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main(num):
    if num == 1:
        urls = [
            f"http://{host1}:{port1}/operacao1/add_new_operation",
            f"http://{host1}:{port2}/operacao2/add_new_operation",
            f"http://{host1}:{port3}/operacao3/add_new_operation",
            f"http://{host1}:{port4}/operacao4/add_new_operation",
        ]
    elif num == 2:
        urls = [
            f"http://{host1}:{port1}/operacao11/add_new_operation",
            f"http://{host1}:{port2}/operacao12/add_new_operation",
            f"http://{host1}:{port3}/operacao13/add_new_operation",
            f"http://{host1}:{port4}/operacao14/add_new_operation",
        ]
    elif num == 3:
        urls = [
            f"http://{host1}:{port1}/operacao15/add_new_operation",
            f"http://{host1}:{port1}/operacao16/add_new_operation",
            f"http://{host1}:{port3}/operacao17/add_new_operation",
            f"http://{host1}:{port3}/operacao18/add_new_operation",

            f"http://{host1}:{port2}/operacao19/add_new_operation",
            f"http://{host1}:{port2}/operacao20/add_new_operation",
            f"http://{host1}:{port4}/operacao21/add_new_operation",
            f"http://{host1}:{port4}/operacao22/add_new_operation",
        ]
    else:
        urls = None
    tasks = [fazer_requisicao(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)

def execution_requests():
    print("\nExecutando outras operações...")
    resp = (requests.get(f"http://{host1}:{port1}/operacao5/add_new_operation"))
    print(resp, resp.json())
    resp = requests.get(f"http://{host1}:{port2}/operacao6/add_new_operation")
    print(resp, resp.json())
    resp = requests.get(f"http://{host1}:{port3}/operacao7/add_new_operation")
    print(resp, resp.json())
    resp = requests.get(f"http://{host1}:{port4}/operacao8/add_new_operation")
    print(resp, resp.json())

    resp = requests.get(f"http://{host1}:{port1}/operacao9/add_new_operation")
    print(resp, resp.json())
    resp = requests.get(f"http://{host1}:{port1}/operacao10/add_new_operation")
    print(resp, resp.json())

def print_lists(one, two, three, four):
    if one == 1:
        resp1 = requests.get(f"http://{host1}:{port1}/return_queues")
        print(resp1, resp1.json())
    if two == 1:
        resp1 = requests.get(f"http://{host1}:{port2}/return_queues")
        print(resp1, resp1.json())
    if three == 1:
        resp1 = requests.get(f"http://{host1}:{port3}/return_queues")
        print(resp1, resp1.json())
    if four == 1:
        resp1 = requests.get(f"http://{host1}:{port4}/return_queues")
        print(resp1, resp1.json())

def print_acks(one, two, three, four):
    if one == 1:
        resp = requests.get(f"http://{host1}:{port1}/return_ack")
        print(resp, f"Lista dos acks do banco {port1}: ", resp.json())
    if two == 1:
        resp = requests.get(f"http://{host1}:{port2}/return_ack")
        print(resp, f"Lista dos acks do banco {port2}: ", resp.json())
    if three == 1:
        resp = requests.get(f"http://{host1}:{port3}/return_ack")
        print(resp, f"Lista dos acks do banco {port3}: ", resp.json())
    if four == 1:
        resp = requests.get(f"http://{host1}:{port4}/return_ack")
        print(resp, f"Lista dos acks do banco {port4}: ", resp.json())

def print_exec(one, two, three, four):
    if one == 1:
        resp1 = requests.get(f"http://{host1}:{port1}/return_executed")
        print(resp1, resp1.json())
    if two == 1:
        resp1 = requests.get(f"http://{host1}:{port2}/return_executed")
        print(resp1, resp1.json())
    if three == 1:
        resp1 = requests.get(f"http://{host1}:{port3}/return_executed")
        print(resp1, resp1.json())
    if four == 1:
        resp1 = requests.get(f"http://{host1}:{port4}/return_executed")
        print(resp1, resp1.json())


#asyncio.run(main(1))

#execution_requests()

#asyncio.run(main(1))

asyncio.run(main(3))

sleep(1)

print("Listas dos bancos:")
print_lists(1, 1, 1, 1)

print("\nListas dos acks:")
print_acks(1, 1, 1, 1)

print("\nListas das operações executadas:")
print_exec(1, 1, 1, 1)
