'''
Arquivo que contém os testes para criação de contas físicas particulares, conjuntas e jurídicas, do administrador e
de outros complementares.
'''

import asyncio
import aiohttp
from os import system, name


system('cls' if name == 'nt' else 'clear')

host1 = "172.16.103.1"
host2 = "172.16.103.2"
host3 = "172.16.103.4"
host4 = "172.16.103.5"

port1 = 5551
port2 = 5552
port3 = 5553
port4 = 5554


async def create_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            return await response.text()


async def main():
    urls = [
        f"http://{host1}:{port1}/maria/08300000000/maria11/maria123/100.0/create_physical_particular",
        f"http://{host2}:{port2}/jose/08500000000/jose11/jose123/200.0/create_physical_joint",
        f"http://{host3}:{port3}/empresa/01400000000000/paula/08400000000/paula11/paula123/300.0/create_juridic_account",
        f"http://{host4}:{port4}/01400000000000/08700000000/paulo/paulo11/paulo123/create_juridic_employeet",
    ]

    tasks = [create_request(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)

asyncio.run(main())
