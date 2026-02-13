# Leitura da lista de inteiros
lista_original = input("Digite os números da lista separados por espaço: ").split()
lista_original = [int(num) for num in lista_original]

# Conjunto para armazenar os elementos únicos
conjunto_elementos_unicos = set()

# Nova lista sem elementos duplicados
lista_sem_duplicados = []

# Percorre a lista original
for num in lista_original:
    # Verifica se o elemento já está no conjunto de elementos únicos
    if num not in conjunto_elementos_unicos:
        # Adiciona o elemento ao conjunto e à nova lista
        conjunto_elementos_unicos.add(num)
        lista_sem_duplicados.append(num)

# Exibição das listas
print("Lista original:", lista_original)
print("Lista sem duplicados:", lista_sem_duplicados)
