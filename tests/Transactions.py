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
            f"http://{host1}:{port1}/08300000000/physical/thi@uefs/50.0/deposit",
            f"http://{host1}:{port1}/08300000000/physical/thi@uefs/100.0/withdraw", # deve ficar com 450
            f"http://{host1}:{port1}/08500000000/physical/77555555555/600.0/withdraw", # não deve executar
            f"http://{host1}:{port1}/08500000000/physical/to9jhgpn577tr55vzhhku55yjz55pkm4/500.0/deposit", # deve ficar com 1000

            f"http://{host1}:{port1}/08300000000/physical_joint/thi@uefs/50.0/deposit",
            f"http://{host1}:{port1}/08500000000/physical_joint/silvio@uefs/100.0/withdraw", # deve ficar com 400
            #
            f"http://{host1}:{port1}/08500000000/juridic/silvio@uefs/50.0/withdraw",
            f"http://{host1}:{port1}/08400000000/juridic/sival@uefs/100.0/deposit", # deve ficar com 550
        ]
    # testes em bancos diferentes
    elif num == 2:
        urls = [
            # bank, cpf, type, key, value, same
            # port_recp, port_send, cpf_recp, cpf_send, type_recp, type_send, key, value, operation,
            # Tentativa de um depósito simples e um saque simples
            f"http://{host1}:{port1}/5551/08300000000/physical/thi@uefs/50.0/1/create_deposit",
            f"http://{host1}:{port1}/5551/08500000000/physical/77555555555/150.0/1/create_deposit",
            f"http://{host1}:{port1}/5551/08300000000/physical/thi@uefs/100.0/2/create_deposit",

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
        resp1 = requests.get(f"http://{host1}:{port1}/return_balances")
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


def create_key():
    requests.get(f"http://{host1}:{port1}/08300000000/physical/email/thi@uefs/create_pix_key")
    requests.get(f"http://{host1}:{port1}/08500000000/physical/phone/77555555555/create_pix_key")
    requests.get(f"http://{host1}:{port1}/08400000000/physical/random/null/create_pix_key")

    requests.get(f"http://{host1}:{port1}/08300000000/physical_joint/email/thi@uefs/create_pix_key")
    requests.get(f"http://{host1}:{port1}/08500000000/physical_joint/email/silvio@uefs/create_pix_key")

    requests.get(f"http://{host1}:{port1}/08500000000/juridic/email/silvio@uefs/create_pix_key")
    requests.get(f"http://{host1}:{port1}/08400000000/juridic/email/sival@uefs/create_pix_key")

    print("\nListas de pix:")
    resp1 = requests.get(f"http://{host1}:{port1}/return_keys")
    print(resp1, f"Lista do banco {port1}: ", resp1.json())


def print_exec(one, two, three, four):
    if one == 1:
        resp1 = requests.get(f"http://{host1}:{port1}/return_executed")
        print(resp1, f"Lista de executadas banco {port1} ", resp1.json())
    if two == 1:
        resp1 = requests.get(f"http://{host1}:{port2}/return_executed")
        print(resp1, resp1.json())
    if three == 1:
        resp1 = requests.get(f"http://{host1}:{port3}/return_executed")
        print(resp1, resp1.json())
    if four == 1:
        resp1 = requests.get(f"http://{host1}:{port4}/return_executed")
        print(resp1, resp1.json())


print("\nSaldos antes das transferências: ")
print_lists(1, 0, 0, 0)

sleep(1)

create_key()

sleep(1)

asyncio.run(main(2))

sleep(1)

print("\nLista dos executados: ")
print_exec(1, 0, 0, 0)

print("\nSaldos após as transferências: ")
print_lists(1, 0, 0, 0)

