# fila.py
class Fila:
    def __init__(self): #Inicializa uma nova instância da classe Pilha
        self.itens = [] #lista usada para armanezar os elementos da fila
                        #Sempre que uma nova fila é criada, essa lista será usada para manter os elementos

    def enfileirar(self, item):  # função para adicionar um novo elemento ao final da fila
        self.itens.append(item) #adicionar o item ao final da lista itenS ao final da pilha

    def desenfileirar(self): #função que Remove e retorna o elemento do inicio da fila
        if not self.esta_vazia(): #verifica se a lkista esta vazia
            return self.itens.pop(0) #remove e retorna o primeiro elemento da lista itens

        else:
            raise IndexError("Desenfileiramento em fila vazia")

    def frente(self): #função que retorna o elemento do início da fila sem removê-lo
        if not self.esta_vazia(): #verifica se a fila esta vazia 
            return self.itens[0] #retorna o primeiro elemento da lista itens
        else:
            raise IndexError("Frente de fila vazia")

    def esta_vazia(self): #verifica se a lista esta vazia
        return len(self.itens) == 0

    def tamanho(self): #tamanho da lista
        return len(self.itens)
