class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def _init_(self):
        self.primeiro = None
        
    def adicionar(self, valor):
        novo_nodo = Nodo(valor)
        if self.primeiro is None:
            self.primeiro = novo_nodo
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def imprimir_recursividade(self):
        self._imprimir_recursivo(self.primeiro) 
        
    def _imprimir_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.valor)
        self._imprimir_recursivo(nodo.proximo)


lista = ListaEncadeada()

lista.adicionar(30)
lista.adicionar(20)
lista.adicionar(10)

lista.imprimir_recursividade()