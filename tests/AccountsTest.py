'''
Arquivo que contém os testes para criação de contas físicas particulares, conjuntas e jurídicas, do administrador e
de outros complementares.
'''

import asyncio
import aiohttp
from os import system, name


system('cls' if name == 'nt' else 'clear')

host1 = "192.168.0.111"
host2 = "172.16.103.1"
host3 = "172.16.103.2"
host4 = "172.16.103.4"
host5 = "172.16.103.5"


port1 = 5551
port2 = 5552
port3 = 5553
port4 = 5554



async def fazer_requisicao(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        f"http://{host1}:{port1}/thiago/08300000000/thi03/thiago123/500.0/create_physical_particular",
        f"http://{host1}:{port1}/silvio/08500000000/sil11/silvio123/500.0/create_physical_joint",
    ]
    tasks = [fazer_requisicao(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)