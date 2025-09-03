import random

def first_fit(head, tamanho, processo_id):
    atual = head
    while atual:
        if not atual.ocupado:
            inicio = atual
            count = 0
            temp = atual
            while temp and not temp.ocupado and count < tamanho:
                count += 1
                temp = temp.next
            if count == tamanho:
                for _ in range(tamanho):
                    inicio.ocupado = True
                    inicio.processo_id = processo_id
                    inicio = inicio.next
                return True
        atual = atual.next
    return False

def best_fit(head, tamanho, processo_id):

    atual = head
    melhor_inicio = None
    melhor_tamanho = None
    melhor_desperdicio = None

    while atual:
        if not atual.ocupado:
            inicio_trecho = atual
            tamanho_trecho = 0
            temp = atual

            while temp and not temp.ocupado:
                tamanho_trecho += 1
                temp = temp.next

            if tamanho_trecho >= tamanho:
                desperdicio = tamanho_trecho - tamanho
                if melhor_inicio is None:
                    melhor_inicio = inicio_trecho
                    melhor_tamanho = tamanho_trecho
                    melhor_desperdicio = desperdicio
                else:

                    if (desperdicio < melhor_desperdicio) or (
                        desperdicio == melhor_desperdicio and tamanho_trecho < melhor_tamanho
                    ):
                        melhor_inicio = inicio_trecho
                        melhor_tamanho = tamanho_trecho
                        melhor_desperdicio = desperdicio

            atual = temp
        else:
            atual = atual.next

    if melhor_inicio is None:
        return False

    marcador = melhor_inicio
    for _ in range(tamanho):
        marcador.ocupado = True
        marcador.processo_id = processo_id
        marcador = marcador.next

    return True

def worst_fit(head, tamanho, processo_id):

    atual = head
    melhor_inicio = None
    melhor_tamanho = 0

    inicio_temp = None
    count = 0

    while atual:
        if not atual.ocupado:
            if inicio_temp is None:
                inicio_temp = atual
                count = 0
            count += 1
        else:

            if count >= tamanho and count > melhor_tamanho:
                melhor_inicio = inicio_temp
                melhor_tamanho = count
            inicio_temp = None
            count = 0
        atual = atual.next

    if count >= tamanho and count > melhor_tamanho:
        melhor_inicio = inicio_temp
        melhor_tamanho = count

    if melhor_inicio is not None:
        marcador = melhor_inicio
        for _ in range(tamanho):
            marcador.ocupado = True
            marcador.processo_id = processo_id
            marcador = marcador.next
        return True

    return False

def liberar_processo(head, processo_id):
    atual = head
    while atual:
        if atual.processo_id == processo_id:
            atual.ocupado = False
            atual.processo_id = None
        atual = atual.next

def liberar_aleatorio(head, processos_ativos):
    if not processos_ativos:
        return None
    pid = random.choice(list(processos_ativos.keys()))
    liberar_processo(head, pid)
    del processos_ativos[pid]
    return pid
