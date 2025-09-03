class Bloco:
    def __init__(self, indice):
        self.indice = indice
        self.ocupado = False
        self.processo_id = None
        self.next = None

def criar_memoria():
    head = Bloco(0)
    atual = head
    for i in range(1, 128):
        novo = Bloco(i)
        atual.next = novo
        atual = novo
    return head

def imprimir_memoria(head):
    atual = head
    memoria = []
    while atual:
        memoria.append(f"[P{atual.processo_id}]" if atual.ocupado else "[ ]")
        atual = atual.next
    print("".join(memoria))

def contar_ocupacao(head):
    atual = head
    usados = 0
    while atual:
        if atual.ocupado:
            usados += 1
        atual = atual.next
    return usados
