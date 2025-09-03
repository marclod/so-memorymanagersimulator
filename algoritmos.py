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
