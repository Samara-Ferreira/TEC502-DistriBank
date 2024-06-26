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


async def fazer_requisicao(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main(num):
    # testes no mesmo banco e criação de contas paralelas
    if num == 1:
        urls = [
            f"http://{host1}:{port1}/thiago/08300000000/thi03/thiago123/110.0/create_physical_particular",
            f"http://{host1}:{port1}/silvio/08500000000/sil11/silvio123/200.0/create_physical_particular",
            f"http://{host1}:{port1}/gustavo/08400000000/guga01/guga123/300.0/create_physical_particular",
        ]
    # testes em bancos diferentes
    elif num == 2:
        urls = [
            f"http://{host1}:{port1}/thiago/08300000000/thi03/thiago123/110.0/create_physical_joint",
            f"http://{host1}:{port1}/08300000000/silvio/08500000000/sil11/silvio123/create_joint_complementary",
            f"http://{host1}:{port1}/08300000000/sival/08400000000/val11/sival123/create_joint_complementary",
        ]
    # testes conta conjunta
    elif num == 3:
        urls = [
            f"http://{host1}:{port1}/netbank/14000000000000/thiago/thi03/08300000000/thiago123/500.0/create_juridic_account",
            f"http://{host1}:{port1}/14000000000000/silvio/sil11/08400000000/silvio123/create_juridic_employee",
        ]
    # testes conta juridica
    elif num == 4:
        urls = [
            f"http://{host1}:{port1}/netbank_thiago/14000000000000_08300000000/thi03/thiago123/500.0/juridic_admin/create_account",
            f"http://{host1}:{port1}/netbank_silvio/08500000000/sil11/silvio123/200.0/juridic_employee/create_account",
            f"http://{host1}:{port1}/netbank_sival/08400000000/val11/sival123/300.0/juridic_employee/create_account",
        ]
    else:
        urls = None
    tasks = [fazer_requisicao(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)


def print_lists(one, two, three, four):
    if one == 1:
        resp1 = requests.get(f"http://{host1}:{port1}/return_clients")
        print(resp1, f"Lista do banco {port1}: ", resp1.json())
    if two == 1:
        resp1 = requests.get(f"http://{host1}:{port2}/return_clients")
        print(resp1, f"Lista do banco {port2}: ", resp1.json())
    if three == 1:
        resp1 = requests.get(f"http://{host1}:{port3}/return_clients")
        print(resp1, f"Lista do banco {port3}: ", resp1.json())
    if four == 1:
        resp1 = requests.get(f"http://{host1}:{port4}/return_clients")
        print(resp1, f"Lista do banco {port4}: ", resp1.json())


asyncio.run(main(2))

sleep(1)

print("\nListas dos bancos:")
print_lists(1, 0, 0, 0)


