# Lista original
lista = [1, 2, 3, 4, 5, 6]
print(lista)
# Tamanho do subgrupo
tamanho_subgrupo = int(input("Digite o tamanho do subgrupo: "))

# Divisão da lista em subgrupos
subgrupos = [lista[i:i+tamanho_subgrupo] for i in range(0, len(lista), tamanho_subgrupo)]

# Exibição dos subgrupos
for subgrupo in subgrupos:
    print(subgrupo)
