from fila import Fila
from pilha import Pilha
    
# ordenar_fila.py
def ordenar_fila(fila):
    #cria duas instancia da classe pilha
    pilha1 = Pilha()
    pilha2 = Pilha()

    # Transferir todos os elementos da fila para a pilha1
    while not fila.esta_vazia(): 
        pilha1.empilhar(fila.desenfileirar()) #remove o elemento da frente da fila 
                                              #e adicona ao topo da pilha

    # Ordenar pilha1 usando pilha2
    while not pilha1.esta_vazia(): 
        temp = pilha1.desempilhar() #remove o elemento do topo de pilha1 (pilha1.desempilhar())
                                    #armazena em temp
        
        # Transferir elementos de pilha2 para pilha1 para encontrar a posição correta
        while not pilha2.esta_vazia() and pilha2.topo() < temp: #se o elemento do topo de pilha2 for menor que temp
            pilha1.empilhar(pilha2.desempilhar()) #remove o elemento do topo de pilha2 e o adiciona de volta a pilha1.
        
        pilha2.empilhar(temp) #Depois que a posição correta para temp for encontrada, adiciona temp ao topo de pilha2
        
    # Transferir os elementos ordenados de pilha2 de volta para a fila
    while not pilha2.esta_vazia():
        fila.enfileirar(pilha2.desempilhar())

# Exemplo de uso
if __name__ == "__main__":
    fila = Fila()

    # Recriar a fila com os mesmos valores
    for valor in [5,8,10,7,25,19,32]:
        fila.enfileirar(valor)

    ordenar_fila(fila)

    print("Fila ordenada:")
    while not fila.esta_vazia():
        print(fila.desenfileirar(), end=" ")
    print()
