import time
import asyncio


async def consulta_dados():
    print("Consultando dados...")
    await asyncio.sleep(2)
    return "dados"


async def processa_dados(dados):
    print("Processando dados...")
    await asyncio.sleep(2)


async def grava_log():
    print("Gravando log...")
    await asyncio.sleep(2)


async def main():
    dados = asyncio.create_task(consulta_dados())
    asyncio.create_task(processa_dados(await dados))
    asyncio.create_task(grava_log())


start = time.perf_counter()
print("Inicio")

asyncio.run(main())

print("Fim")
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")