class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.first = None

    def cria(self):
        self.first = None

    def insere(self, valor, posicao):
        novo_nodo = Nodo(valor)
        if posicao == 0:
            novo_nodo.proximo = self.first
            self.first = novo_nodo
        else:
            atual = self.first
            indice = 0
            while atual is not None and indice < posicao - 1:
                atual = atual.proximo
                indice += 1
            if atual is None:
                raise IndexError("Posição fora dos limites da lista.")
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def remove(self, posicao):
        if self.first is None:
            raise IndexError("Lista vazia.")
        if posicao == 0:
            self.first = self.first.proximo
        else:
            atual = self.first
            indice = 0
            while atual.proximo is not None and indice < posicao - 1:
                atual = atual.proximo
                indice += 1
            if atual.proximo is None:
                raise IndexError("Posição fora dos limites da lista.")
            atual.proximo = atual.proximo.proximo

    def posicao(self, valor):
        return self._posicao_recursiva(self.first, valor, 0)

    def _posicao_recursiva(self, no, valor, indice):
        if no is None:
            return -1  # Valor não encontrado
        if no.valor == valor:
            return indice
        return self._posicao_recursiva(no.proximo, valor, indice + 1)

    def valor(self, posicao):
        atual = self.first
        indice = 0
        while atual is not None:
            if indice == posicao:
                return atual.valor
            atual = atual.proximo
            indice += 1
        raise IndexError("Posição fora dos limites da lista.")

    def destroi(self):
        self.first = None

    def imprimir(self):
        atual = self.first
        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")


# Exemplo de uso do TAD Lista Encadeada
lista = ListaEncadeada()
lista.insere(10, 0)
lista.insere(20, 1)
lista.insere(30, 2)
lista.insere(40, 3)

lista.imprimir()  # Saída: 10 -> 20 -> 30 -> 40 -> None

print("Posição do valor 30:", lista.posicao(30))  # Saída: Posição do valor 30: 2
print("Posição do valor 50:", lista.posicao(50))  # Saída: Posição do valor 50: -1 (não encontrado)


