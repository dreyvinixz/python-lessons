# Leitura da frase
frase = input("Digite uma frase: ")

# Leitura da chave
try:
    chave = int(input("Digite a chave de criptografia: "))
except ValueError:
    print("Invalid")

# Criptografia da frase
frase_criptografada = ""
for caractere in frase:
    if caractere.isalpha():
        codigo = ord(caractere)
        if caractere.isupper():
            codigo_base = ord('A')
            num_letras = 26
        else:
            codigo_base = ord('a')
            num_letras = 26
        codigo_criptografado = (codigo - codigo_base + chave) % num_letras + codigo_base
        caractere_criptografado = chr(codigo_criptografado)
        frase_criptografada += caractere_criptografado
    else:
        frase_criptografada += caractere

# Exibição da frase criptografada
print("Frase criptografada:", frase_criptografada)
