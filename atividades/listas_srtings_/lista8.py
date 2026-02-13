# Leitura da frase
frase = input("Digite uma frase: ")

# Contagem de caracteres
quantidade_caracteres = len(frase)

# Contagem de palavras
palavras = frase.split()
quantidade_palavras = len(palavras)

# Exibição dos resultados
print("Quantidade de caracteres:", quantidade_caracteres)
print("Quantidade de palavras:", quantidade_palavras)
