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
        async with session.post(url) as response:
            return await response.text()


async def main(op1, op2):
    urls = [
        f"http://{host1}:{port1}/{op1}/create_transfer",
        f"http://{host1}:{port1}/{op2}/create_transfer",
    ]
    tasks = [fazer_requisicao(url) for url in urls]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        print(resultado)

operation1 = {"host_recp": host1, "port_recp": port2, "cpf_recp": "08600000000", "type_recp": "physical",
                         "key_recp": "gu@",
                         "host_send": host1, "port_send": port1, "cpf_send": "08500000000", "type_send": "physical",
                         "value": 150.0, "operation": "transfer"}

operation2 = {"host_recp": host1, "port_recp": port3, "cpf_recp": "08700000000", "type_recp": "physical",
                         "key_recp": "gui@",
                         "host_send": host1, "port_send": port1, "cpf_send": "08500000000", "type_send": "physical",
                         "value": 60.0, "operation": "transfer"}

asyncio.run(main([operation1], [operation2]))
