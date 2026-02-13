class ListaContinua:
    def __init__(self):
        self.lista = []
        self.mostrar_estado("Inicializa")

    def inserir(self, posicao, elemento):
        if 1 <= posicao <= len(self.lista) + 1:
            self.lista.insert(posicao - 1, elemento)
        else:
            print(f"Posição {posicao} inválida!")
        self.mostrar_estado(f"Insere ({posicao}, {elemento})")

    def remover(self, posicao):
        if 1 <= posicao <= len(self.lista):
            removido = self.lista.pop(posicao - 1)
            self.mostrar_estado(f"Remove ({posicao}) -> {removido}")
        else:
            print(f"Posição {posicao} inválida para remoção!")
    
    def consulta(self, posicao):
        if 1 <= posicao <= len(self.lista):
            return self.lista[posicao - 1]
        else:
            print(f"Posição {posicao} inválida para consulta!")
            return None
    
    def buscar(self, valor):
        for i, elemento in enumerate(self.lista):
            if elemento == valor:
                return i + 1  # Retorna a posição (1-based index)
        return -1  # Retorna -1 se o valor não for encontrado
    
    def destruir(self):
        self.lista = []
        self.mostrar_estado("Destrói")
    
    def mostrar_estado(self, operacao):
        print(f"{operacao}: {self.lista}")

# Criando e manipulando a lista
lista = ListaContinua()
lista.inserir(1, "Carro")
lista.inserir(2, "Moto")
lista.inserir(2, "Bicicleta")
lista.remover(3)
lista.inserir(10, "Caminhão")  # Esta operação falhará
item = lista.consulta(2)
lista.inserir(1, item if item else "")
item = lista.consulta(2)
lista.inserir(1, item if item else "")
print("Posição de 'Bicicleta':", lista.buscar("Bicicleta"))
lista.destruir()
