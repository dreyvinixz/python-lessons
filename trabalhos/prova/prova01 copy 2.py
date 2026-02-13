def entrada(idade):
    if idade < 0:
        return "Erro: Idade inválida."
    elif idade < 5:
        return "Entrada gratuita para crianças pequenas."
    elif idade < 12:
        return "Entrada de crianças: R$ 10,00."
    elif idade < 18:
        return "Entrada de adolescentes: R$ 15,00."
    else:
        return "Entrada de adultos: R$ 20,00."

try:
    idade = int(input("Digite a idade do visitante: ")
                     )
    mensagem = entrada(idade)
    print(mensagem)
except ValueError:
     print("Erro: Por favor, digite um valor válido para a idade.")