class Lista:
    def __init__(self):
        self.lista = []
    
    def iniciar(self):
        """
        Inicializa a lista, tornando-a vazia.
        """
        self.lista = []
    
    def inserir_na_posicao(self, i, produto):
        """
        Insere um produto na posição i.
        
        :param i: Posição onde o produto deve ser inserido.
        :param produto: Produto a ser inserido.
        """
        if i < 0 or i > len(self.lista):
            raise IndexError("Índice fora dos limites da lista.")
        self.lista.insert(i, produto)
    
    def remover_da_posicao(self, i):
        """
        Remove o produto da posição i.
        
        :param i: Posição do produto a ser removido.
        """
        if i < 0 or i >= len(self.lista):
            raise IndexError("Índice fora dos limites da lista.")
        self.lista.pop(i)
    
    def localizar_posicao(self, produto):
        """
        Localiza a posição de um produto na lista.
        
        :param produto: Produto a ser localizado.
        :return: Posição do produto na lista ou -1 se não encontrado.
        """
        try:
            return self.lista.index(produto)
        except ValueError:
            return -1
    
    def limpar(self):
        """
        Limpa a lista, excluindo todos os elementos.
        """
        self.lista = []

    def __repr__(self):
        return str(self.lista)

# Exemplo de uso
lista_produtos = Lista()

# Iniciar a lista
lista_produtos.iniciar()
print("Após iniciar:", lista_produtos)

# Inserir produtos
lista_produtos.inserir_na_posicao(0, "Produto A")
lista_produtos.inserir_na_posicao(1, "Produto B")
lista_produtos.inserir_na_posicao(1, "Produto C")
print("Após inserções:", lista_produtos)

# Remover produto da posição 1
lista_produtos.remover_da_posicao(1)
print("Após remover da posição 1:", lista_produtos)

# Localizar posição de um produto
posicao = lista_produtos.localizar_posicao("Produto A")
print("Posição do 'Produto A':", posicao)

# Limpar a lista
lista_produtos.limpar()
print("Após limpar:", lista_produtos)
