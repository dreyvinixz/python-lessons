def calcular_aproximacao_pi(numero_termos):
    aproximacao_pi = 0.0
    sinal = 1

    for i in range(1, numero_termos * 2, 2):
        termo = 1 / i * sinal
        aproximacao_pi += termo
        sinal *= -1

    aproximacao_pi *= 4
    return aproximacao_pi

# Solicitar ao usuário o número de termos
try:
    numero_termos = int(input("Digite o número de termos para a aproximação de pi: "))
    
    if numero_termos <= 0:
        print("Por favor, insira um número de termos positivo.")
    else:
        resultado_aproximacao = calcular_aproximacao_pi(numero_termos)
        print(f"Aproximação de pi com {numero_termos} termos: {resultado_aproximacao}")
except ValueError:
    print("Erro: Por favor, digite um valor válido para o valor!")
    