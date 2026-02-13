class Vertex:
    def __init__(self, key, value):
        self.id = key
        self.value = value
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key, value):
        self.numVertices += 1
        newVertex = Vertex(key, value)
        self.vertList[key] = newVertex
        return newVertex

    def removeVertex(self, key):
        if key in self.vertList:
            for v in self.vertList.values():
                if self.vertList[key] in v.connectedTo:
                    del v.connectedTo[self.vertList[key]]
            del self.vertList[key]
            self.numVertices -= 1

    def getVertex(self, key):
        return self.vertList.get(key, None)

    def addEdge(self, f, t, weight=0):
        if f in self.vertList and t in self.vertList:
            self.vertList[f].addNeighbor(self.vertList[t], weight)

    def removeEdge(self, f, t):
        if f in self.vertList and t in self.vertList:
            if self.vertList[t] in self.vertList[f].connectedTo:
                del self.vertList[f].connectedTo[self.vertList[t]]

    def areAdjacent(self, f, t):
        if f in self.vertList and t in self.vertList:
            return self.vertList[t] in self.vertList[f].connectedTo
        return False

    def getIncidences(self, key):
        incidences = []
        for v in self.vertList.values():
            if self.vertList[key] in v.connectedTo:
                incidences.append(v.getId())
        return incidences

    def getVertices(self):
        return self.vertList.keys()

    def listEdges(self):
        edges = []
        for v in self.vertList.values():
            for w in v.getConnections():
                edges.append((v.getId(), w.getId(), v.getWeight(w)))
        return edges


# Criando um grafo e adicionando vértices
g = Graph()
for i in range(6):
    g.addVertex(i, "V" + str(i))

# Adicionando arestas com pesos
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 2)
g.addEdge(0, 3, 4)
g.addEdge(0, 4, 9)
g.addEdge(2, 6, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 7, 1)
g.addEdge(1, 8, 8)
g.addEdge(5, 2, 1)

# Iterando pelos vértices e imprimindo conexões
for v in g:
    for w in v.getConnections():
        print("( %s , %s , %d )" % (v.getId(), w.getId(), v.getWeight(w)))

# Exemplo de uso dos métodos adicionados
print("\nVértices adjacentes do vértice 3:", g.getAdjacentVertices(0))
g.printAdjacencyWeights(3)

# Executando as buscas
print("\nExecutando Busca em Largura (BFS) a partir do vértice 0:")
g.bfs(0)

print("\nExecutando Busca em Profundidade (DFS) a partir do vértice 0:")
g.dfs(0)
