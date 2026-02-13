def num_1 (idade):
    if idade <= 0:
        return "zero"
    if idade < 5:
        return "entrada"
    if idade < 12:
        return "paga"

entrada = int(input("digite :"))
mensagem = num_1(entrada)
print(mensagem)