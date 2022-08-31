import time

def calcula_tempo(funcao):
    def wrapper():
        tempo_inicio = time.time()
        funcao()
        tempo_final = time.time()
        
        calculo = tempo_final - tempo_inicio
        
        print(f'A função {funcao.__name__}, levou o total de {calculo} para ser executada')
        
        return wrapper
@calcula_tempo
def run():
    for n in range(10000):
        yield

run()

              
              