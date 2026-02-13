from list1_encadeada import ListaEncadeada

def teste_lista():
    lista = ListaEncadeada()
    
    # Insere valores
    lista.insere(10, 0)
    lista.insere(20, 1)
    lista.insere(30, 2)
    
    # Testa valor
    assert lista.valor(0) == 10
    assert lista.valor(1) == 20
    assert lista.valor(2) == 30
    
    # Testa posição
    assert lista.posicao(10) == 0
    assert lista.posicao(20) == 1
    assert lista.posicao(30) == 2
    
    # Remove valor
    lista.remove(1)
    assert lista.valor(1) == 30
    
    # Testa posição após remoção
    assert lista.posicao(20) == -1
    
    # Destroi lista
    lista.destroi()
    assert lista.tamanho == 0

if __name__ == "__main__":
    teste_lista()
    print("Todos os testes passaram!")
