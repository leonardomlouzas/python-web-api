import time
import concurrent.futures


def consulta_dados():
    print("Consultando dados...")
    time.sleep(2)
    return "dados"


def processa_dados(dados):
    print("Processando dados...")
    time.sleep(2)


def grava_log():
    print("Gravando log...")
    time.sleep(2)


def main():
    start = time.perf_counter()
    print("Inicio")

    with concurrent.futures.ProcessPoolExecutor() as executer:    
        future = executer.submit(consulta_dados)
        dados = future.result()
        executer.submit(processa_dados, dados)
        executer.submit(grava_log)
        executer.submit(grava_log)
        executer.submit(grava_log)
        executer.submit(grava_log)
        executer.submit(grava_log)

    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")


main()
