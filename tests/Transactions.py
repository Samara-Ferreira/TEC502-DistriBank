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
            f"http://{host1}:{port1}/08300000000/physical_joint/phone/77555555555/create_pix_key",
            f"http://{host1}:{port1}/08300000000/physical_joint/random/null/create_pix_key",
            f"http://{host1}:{port1}/08500000000/physical_joint/random/null/create_pix_key",
            f"http://{host1}:{port1}/08400000000/physical_joint/email/sival@uefs/create_pix_key",

            f"http://{host1}:{port1}/09100000000/physical/cpf_cnpj/09100000000/create_pix_key",
        ]
    # testes em bancos diferentes
    elif num == 2:
        urls = [

        ]
    # testes conta conjunta
    elif num == 3:
        urls = [

        ]
    # testes conta juridica
    elif num == 4:
        urls = [

        ]
    else:
        urls = None
    tasks = [fazer_requisicao(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)


def print_lists(one, two, three, four):
    if one == 1:
        resp1 = requests.get(f"http://{host1}:{port1}/return_keys")
        print(resp1, f"Lista do banco {port1}: ", resp1.json())
    if two == 1:
        resp1 = requests.get(f"http://{host1}:{port2}/return_keys")
        print(resp1, f"Lista do banco {port2}: ", resp1.json())
    if three == 1:
        resp1 = requests.get(f"http://{host1}:{port3}/return_keys")
        print(resp1, f"Lista do banco {port3}: ", resp1.json())
    if four == 1:
        resp1 = requests.get(f"http://{host1}:{port4}/return_keys")
        print(resp1, f"Lista do banco {port4}: ", resp1.json())


requests.get(f"http://{host1}:{port1}/thiago/08300000000/thi03/thiago123/110.0/create_physical_joint")
requests.get(f"http://{host1}:{port1}/08300000000/silvio/08500000000/sil11/silvio123/create_joint_complementary")
requests.get(f"http://{host1}:{port1}/08300000000/sival/08400000000/val11/sival123/create_joint_complementary")

requests.get(f"http://{host1}:{port1}/gustavo/09100000000/guga01/guga123/300.0/create_physical_particular")
requests.get(f"http://{host1}:{port1}/guilherme/09200000000/gui03/gui123/200.0/create_physical_particular")

requests.get(f"http://{host1}:{port1}/netbank/14000000000000/thiago/thi03/08300000000/thiago123/500.0/create_juridic_account")
requests.get(f"http://{host1}:{port1}/14000000000000/silvio/sil11/08700000000/silvio123/create_juridic_employee")

asyncio.run(main(1))

sleep(1)

print("\nListas dos clientes:")
resp1 = requests.get(f"http://{host1}:{port1}/return_clients")
print(resp1, f"Lista do banco {port1}: ", resp1.json())

print("\nListas dos bancos:")
print_lists(1, 0, 0, 0)




