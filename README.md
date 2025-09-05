# Gerenciador de Memória

### Como rodar

No terminal, a partir da pasta do projeto, execute:

```bash
python main.py
```

O programa inicia a simulação e imprime o andamento no terminal até a simulação ser finalizada manualmente ou atingir seu fim programado. Caso precise ajustar parâmetros (limiares, tamanho da memória, etc.), edite as constantes no arquivo `simulador.py`.

## Estrutura base

- Memória: lista encadeada com 128 nós (índices 0..127).
- Granularidade: 1 nó = 1 KB. Dois nós consecutivos = 1 bloco lógico = 2 KB (64 blocos lógicos).
- Conteúdo do nó: índice, estado (livre / ocupado), identificador do processo.

### Regras de alocação

1. Calcular quantos nós de 1 KB são necessários para o pedido.
2. Reservar uma sequência contígua de nós e marcar como ocupados.
3. Se o número de nós for ímpar, o último bloco lógico pode ficar parcialmente vazio.

### Fluxo do loop

- Sortear tamanho do pedido.
- Escolher algoritmo (adaptativo).
- Tentar alocar com o algoritmo escolhido.
- Se falhar: aplicar rotina de liberação (por exemplo, liberar processo aleatório) para criar espaço.
- Repetir até parada manual ou fim da simulação.

### Arquivos principais

- `memoria.py`: definição de `Bloco` e `criar_memoria()` (lista encadeada de 128 nós).
- `algoritmos.py`: implementação de `first_fit`, `best_fit`, `worst_fit` e rotinas de liberação.
- `simulador.py`: loop principal e função `escolher_algoritmo(memoria)` que decide qual algoritmo usar.
- `main.py`: ponto de entrada que inicializa a simulação.

## Algoritmo adaptativo: escolhas e justificativas

A seleção do algoritmo é feita com base na ocupação atual da memória (percentual de nós ocupados):

- Ocupação < 40% usa **First Fit**
- 40% ≤ Ocupação < 75% usa **Best Fit**
- Ocupação ≥ 75% usa **Worst Fit**

**Por que essa ordem (First / Best / Worst)?**

- **First Fit (baixa ocupação):** é mais rápido quando há muito espaço livre; encontra o primeiro trecho que serve, com custo baixo.
- **Best Fit (ocupação média):** quando a memória começa a ficar fragmentada, escolher o trecho mais próximo do tamanho do pedido reduz o desperdício imediato.
- **Worst Fit (ocupação alta):** com pouca memória livre, alocar em trechos grandes evita quebrar os últimos blocos grandes em muitos pedaços pequenos, preservando capacidade para pedidos maiores no futuro.

## Considerações e escolhas

- **Complexidade:** First Fit e Best Fit podem percorrer toda a lista no pior caso (O(n)). Worst Fit também requer varredura para achar o maior bloco. O tempo real depende da ocupação e do padrão de espaços livres.
- **Fragmentação:** Best Fit tende a reduzir espaço sobrando imediatamente, mas pode gerar buracos pequenos. Worst Fit tenta evitar buracos pequenos usando trechos maiores.
- **Parâmetros:** os limites (40% e 75%) são um compromisso prático e podem ser ajustados conforme a carga desejada:
  - Priorizar rapidez em baixa ocupação: diminuir o limite inferior.
  - Reduzir fragmentação em ocupação média: ajustar a faixa do Best Fit.
  - Preservar blocos grandes em ocupação alta: ajustar o limite superior.
