def calcular(numero_termos):
    aprox = 0.0
    sinal = 1

    for i in range(1, numero_termos * 2, 2):
        termo = 1 / i * sinal
        aprox += termo
        sinal *= -1
    aprox *= 4
    return aprox

entrada = int(input(""))

if entrada <= 0:
    print("A"
          )
else:
    resut_aprox = calcular(entrada)
    print("b")