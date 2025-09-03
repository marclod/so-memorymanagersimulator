import random
import time
import math
from memoria import criar_memoria, imprimir_memoria, contar_ocupacao
from algoritmos import first_fit, liberar_aleatorio

def simulador(tempo_exec=60):
    memoria = criar_memoria()
    processos_ativos = {}
    processo_id = 1
    inicio = time.time()
    processo_pendente = None  # guarda o processo que falhou

    while time.time() - inicio < tempo_exec:
        if processo_pendente:
            # Se existe processo pendente tentar novamente
            pid, tamanho = processo_pendente
            print(f"\nTentando novamente alocar processo {pid} (tamanho {tamanho} nos).")
            blocos = tamanho // 2
            processo_pendente = None
        else:
            # Gera novo processo em KB
            kb = random.randint(1, 16) 
            tamanho = math.ceil(kb / 2)  # cada nó = 2KB
            print(f"\nNovo processo {processo_id} pede {kb} KB -> {tamanho} nos necessarios")

        sucesso = first_fit(memoria, tamanho, processo_id)

        if not sucesso:
            print(f"Sem espaco! Removendo processo aleatorio...")
            pid_removido = liberar_aleatorio(memoria, processos_ativos)
            if pid_removido:
                print(f"Processo {pid_removido} removido.")
            # tenta de novo o mesmo processo
            sucesso = first_fit(memoria, tamanho, processo_id)

        if sucesso:
            processos_ativos[processo_id] = tamanho
            print(f"Processo {processo_id} alocado com sucesso!")
            processo_id += 1  # só incrementa se realmente entrou
        else:
            print(f"Nao foi possivel alocar processo {processo_id}. Ficara pendente.")
            processo_pendente = (processo_id, tamanho)

        usados = contar_ocupacao(memoria)
        percentual = (usados / 128) * 100
        print(f"Total de memoria alocada: {percentual:.2f}%")
        imprimir_memoria(memoria)

        time.sleep(1)

    print("\n--- Simulacao encerrada ---")
