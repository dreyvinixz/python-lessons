import networkx as nx
import matplotlib.pyplot as plt
import time

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def draw_graph_step(graph, mst_edges, current_edge=None, edge_labels=None, pos=None, title=""):
    """
    Desenha o grafo com as arestas da MST destacadas em vermelho e a aresta atual em verde.
    """
    plt.figure(figsize=(8, 6))

    # Desenha todas as arestas do grafo em cinza
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')

    # Destaque das arestas da MST em vermelho
    nx.draw_networkx_edges(graph, pos, edgelist=mst_edges, edge_color='red', width=2)

    # Destaque da aresta atual em verde
    if current_edge:
        nx.draw_networkx_edges(graph, pos, edgelist=[current_edge], edge_color='green', width=2)

    # Exibe os pesos das arestas sobre as linhas
    if edge_labels:
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.show()
    time.sleep(1)  # Pausa para visualização

def kruskal_visualization(graph_data):
    """
    Implementa o Algoritmo de Kruskal com visualização passo a passo.
    """
    # Criando o grafo com NetworkX
    graph = nx.Graph()
    for u in graph_data:
        for v, w in graph_data[u]:
            graph.add_edge(u, v, weight=w)

    edges = [(u, v, d['weight']) for u, v, d in graph.edges(data=True)]
    edges.sort(key=lambda x: x[2])  # Ordena as arestas por peso
    vertices = list(graph.nodes)
    
    disjoint_set = DisjointSet(vertices)
    mst_edges = []  # Lista de arestas da MST

    # Calcular o layout do grafo uma única vez
    pos = nx.spring_layout(graph)

    print("### Execução do Algoritmo de Kruskal ###")
    draw_graph_step(graph, mst_edges, pos=pos, title="Grafo Inicial")

    # Preparar os rótulos das arestas com seus pesos
    edge_labels = { (u, v): graph[u][v]['weight'] for u, v in graph.edges() }

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_edges.append((u, v))
            print(f"Aresta adicionada: ({u}, {v}) - Peso: {weight}")
            draw_graph_step(graph, mst_edges, current_edge=(u, v), edge_labels=edge_labels, pos=pos, title=f"Processando Aresta: ({u}, {v}) - Peso: {weight}")
    
    print("\n### Árvore Geradora Mínima Final ###")
    for u, v in mst_edges:
        print(f"Aresta: ({u}, {v}) - Peso: {graph[u][v]['weight']}")
    
    draw_graph_step(graph, mst_edges, edge_labels=edge_labels, pos=pos, title="Árvore Geradora Mínima Final")

# Exemplo de uso
if __name__ == "__main__":
    # Representação do grafo: {vértice: [(vizinho, peso), ...]}
    graph_data = {
        'A': [('B', 1), ('D', 4)],
        'B': [('A', 1), ('C', 3), ('D', 2)],
        'C': [('B', 3), ('D', 5), ('E', 6)],
        'D': [('A', 4), ('B', 2), ('C', 5), ('E', 7)],
        'E': [('C', 6), ('D', 7)]
    }

    kruskal_visualization(graph_data)
