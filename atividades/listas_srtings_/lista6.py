print("Modelo de Conta = 0000-0")
# Leitura do número da conta
conta = input("Digite o número da conta: ")

# Remoção do caractere "-"
conta = conta.replace("-", "")

# Cálculo do dígito verificador
soma_digitos = sum(int(digito) for digito in conta)
digito_verificador = soma_digitos % 10

# Verificação da validade da conta
if digito_verificador == int(conta[-1]):
    print("Conta válida!")
else:
    print("Conta inválida!")
