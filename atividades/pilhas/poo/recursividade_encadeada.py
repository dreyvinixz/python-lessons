class Nodo:
    def __init__(self, valor):
        self.valor = valor #Armazena o valor do nó
        self.proximo = None #Um ponteiro para o próximo nó na lista encadeada

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None #inicializa uma lista vazia
        
    def adicionar(self, valor): 
        new_nodo = Nodo(valor) #new nó
        if self.primeiro is None:
            self.primeiro = new_nodo
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = new_nodo #new nó e adiconado apos o ultimo

    def imprimir(self):
        atual = self.primeiro
        while atual is not None: #Começa do primeiro nó e imprime o valor de cada nó
            print(atual.valor)
            atual = atual.proximo

    def imprimir_recursivamente(self):
        self._imprimir_recursivo(self.primeiro) 
        
    def _imprimir_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.valor)
        self._imprimir_recursivo(nodo.proximo)

    def posicao_recursiva(self, nodo, valor, indice):
        if nodo is None:
            return -1
        if nodo.valor == valor:
            return indice
        return self.posicao_recursiva(nodo.proximo, valor, indice + 1)

    def posicao(self, valor):
        return self.posicao_recursiva(self.primeiro, valor, 0)


# Criando e testando a lista encadeada
lista = ListaEncadeada()
lista.adicionar(30)
lista.adicionar(20)
lista.adicionar(10)

# Imprimindo a lista usando o método recursivo
lista.imprimir_recursivamente()

# Buscando e imprimindo a posição dos valores
print("Posição do valor 30:", lista.posicao(30))  # Saída: Posição do valor 30: 0
print("Posição do valor 20:", lista.posicao(20))  # Saída: Posição do valor 20: 1
print("Posição do valor 10:", lista.posicao(10))  # Saída: Posição do valor 10: 2
print("Posição do valor 40:", lista.posicao(40))  # Saída: Posição do valor 40: -1 (não encontrado)
