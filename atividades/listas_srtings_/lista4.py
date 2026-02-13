# Leitura da string
string = input("Digite uma string: ")

# Leitura da letra a ser substituída
letra_antiga = input("Digite a letra a ser substituída: ")

# Leitura da letra nova
letra_nova = input("Digite a letra nova: ")

# Substituição da letra na string
nova_string = string.replace(letra_antiga, letra_nova)

# Exibição da nova string
print("Nova string:", nova_string)
