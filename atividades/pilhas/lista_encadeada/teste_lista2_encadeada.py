# teste_lista_encadeada.py

from list2_encadeada import ListaEncadeada

def teste_lista():
    lista1 = ListaEncadeada()
    lista2 = ListaEncadeada()
    
    # Insere valores nas duas listas
    lista1.insere(10, 0)
    lista1.insere(20, 1)
    lista1.insere(30, 2)

    lista2.insere(10, 0)
    lista2.insere(20, 1)
    lista2.insere(30, 2)

    # Testa número de elementos
    assert lista1.numero_elementos() == 3
    
    # Testa se as listas são iguais
    assert lista1.sao_iguais(lista2) == True

    # Modifica a segunda lista e testa novamente
    lista2.insere(40, 3)
    assert lista1.sao_iguais(lista2) == False

    # Imprime a lista invertida
    print("Lista 1 invertida: ")
    lista1.imprime_invertido()
    
    # Destroi a lista e verifica se está vazia
    lista1.destroi()
    assert lista1.numero_elementos() == 0

if __name__ == "__main__":
    teste_lista()
    print("Todos os testes passaram!")
