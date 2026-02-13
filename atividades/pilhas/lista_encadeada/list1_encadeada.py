# lista_encadeada.py

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def insere(self, valor, posicao):
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição fora do intervalo")

        novo_nodo = Nodo(valor)

        if posicao == 0:
            novo_nodo.proximo = self.cabeca 
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            for _ in range(posicao - 1):
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

        self.tamanho += 1

    def remove(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição fora do intervalo")

        if posicao == 0:
            self.cabeca = self.cabeca.proximo
        else:
            atual = self.cabeca
            for _ in range(posicao - 1):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo

        self.tamanho -= 1

    def posicao(self, valor):
        atual = self.cabeca
        pos = 0
        while atual is not None:
            if atual.valor == valor:
                return pos
            atual = atual.proximo
            pos += 1
        return -1

    def valor(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição fora do intervalo")

        atual = self.cabeca
        for _ in range(posicao):
            atual = atual.proximo
        return atual.valor

    def destroi(self):
        self.cabeca = None
        self.tamanho = 0


