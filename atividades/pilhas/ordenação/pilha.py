# pilha.py
class Pilha: #class pilha
    def __init__(self): #Inicializa uma nova instância da classe Pilha.
        self.itens = [] #lista usada para armanezar os elementos da pilha
                        #sempre que uma pilha e criada esssa lista sera usada para manter os elementos

    def empilhar(self, item): # função para adicionar um novo elemento ao topo da pilha.
        self.itens.append(item) #adicionar o item ao final da lista itenS O TOPO da pilha
                                #sempre que um novo elemento for inserido ira seguir a regra lifo

    def desempilhar(self): #função que Remove e retorna o elemento do topo da pilha.
        if not self.esta_vazia(): #verifica se a pilha não esta vazia 
            return self.itens.pop() #remove e retorna o último elemento da lista itens usando o método pop.
        else:
            raise IndexError("Desempilhaxmento em pilha vazia")

    def topo(self): #função que retorna o elemento do topo da pilha sem removê-lo.
        if not self.esta_vazia(): #verifica se a pilha não esta vazia
            return self.itens[-1] #Se a pilha não estiver vazia, retorna o último elemento da lista itens.

        else:
            raise IndexError("Topo de pilha vazia")

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)