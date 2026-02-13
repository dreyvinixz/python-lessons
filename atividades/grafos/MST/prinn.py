import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time

def prim_mst_visual(graph, weights, root):
    """
    Implementação do algoritmo de Prim com visualização gráfica.

    Parâmetros:
    - graph: Um dicionário representando o grafo {vértice: [vizinhos]}.
    - weights: Um dicionário de pesos {(u, v): peso}.
    - root: O vértice inicial da MST.
    """
    # Inicialização
    key = {u: float('inf') for u in graph}  # Valores-chave iniciais como infinito
    parent = {u: None for u in graph}      # Predecessor de cada vértice
    visited = set()                        # Conjunto de vértices incluídos na MST
    key[root] = 0                          # Chave do vértice raiz como 0

    # Fila de prioridade (min-heap), contendo (peso, vértice)
    priority_queue = [(0, root)]

    mst_edges = []  # Lista para armazenar as arestas da MST

    # Criando o grafo com NetworkX
    G = nx.Graph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, weight=weights[(u, v)])

    # Layout do grafo para visualização
    pos = nx.spring_layout(G)

    # Visualização inicial
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo Original")
    plt.show()

    step = 1  # Contador de etapas

    while priority_queue:
        weight_u, u = heapq.heappop(priority_queue)

        if u in visited:
            continue

        visited.add(u)
        print(f"\n### Passo {step} ###")
        print(f"Processando vértice: {u} (Peso: {weight_u})")

        # Adiciona a aresta à MST se tiver um pai
        if parent[u] is not None:
            mst_edges.append((parent[u], u))
            print(f"Aresta adicionada à MST: ({parent[u]}, {u}) - Peso: {weight_u}")

        # Atualiza os vizinhos
        for v in graph[u]:
            if v not in visited and weights[(u, v)] < key[v]:
                key[v] = weights[(u, v)]
                parent[v] = u
                heapq.heappush(priority_queue, (key[v], v))

        # Visualização gráfica do progresso
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Desenha as arestas da MST em destaque
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)

        plt.title(f"Execução do Algoritmo de Prim - Passo {step}")
        plt.show()

        time.sleep(1)  # Pausa para visualização
        step += 1

    print("\n### Árvore Geradora Mínima Final ###")
    for u, v in mst_edges:
        print(f"Aresta: ({u}, {v}) - Peso: {weights[(u, v)]}")
    
    return mst_edges

# Exemplo de uso
if __name__ == "__main__":
    # Representação do grafo
    graph = {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'D', 'E'],
        'D': ['A', 'B', 'C', 'E'],
        'E': ['C', 'D']
    }
    
    # Pesos das arestas
    weights = {
        ('A', 'B'): 1, ('B', 'A'): 1,
        ('A', 'D'): 4, ('D', 'A'): 4,
        ('B', 'C'): 3, ('C', 'B'): 3,
        ('B', 'D'): 2, ('D', 'B'): 2,
        ('C', 'D'): 5, ('D', 'C'): 5,
        ('C', 'E'): 6, ('E', 'C'): 6,
        ('D', 'E'): 7, ('E', 'D'): 7
    }
    
    # Executa o algoritmo
    root = 'A'
    prim_mst_visual(graph, weights, root)
