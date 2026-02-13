# Leitura das duas sequências ordenadas
sequencia1 = input("Digite os elementos da primeira sequência ordenada: ")
sequencia2 = input("Digite os elementos da segunda sequência ordenada: ")

# Combinação das sequências ordenadas
sequencia_combinada = sequencia1 + sequencia2

# Ordenação da sequência combinada em ordem crescente usando sorted
sequencia_ordenada = sorted(sequencia_combinada)

# Exibição dos elementos em ordem crescente
print("Elementos em ordem crescente:")
print(*sequencia_ordenada)
