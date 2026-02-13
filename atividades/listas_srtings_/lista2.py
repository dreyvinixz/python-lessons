#listas vazias

lista1 = []
lista2 = []
lista3 = []

# obter o tamnaho da lista
while True:
    try:
        tamanho = int(input("Digite o tamanho da lista: "))
        if tamanho <= 0:
            print("tamanho da lista deve ser maior que 0")
            break
        else:
            for i in range(tamanho):
                elemento1 = int(input("Digite um elemento para a lista 1: "))
                lista1.append(elemento1)
            for i in range(tamanho):
                elemento2 = int(input("Digite um elemento para a lista 2: "))
                lista2.append(elemento2)
            for i in range(tamanho):
                elemento3 = int(input("Digite um elemento para a lista 3: "))
                lista3.append(elemento3)
    except ValueError:
        print("Por Favor, digite um valor inteiro positivo")
        break
    # a) Números maiores que 5
    print("Números maiores que 5:")
    for i, elemento in enumerate(lista1):
        if elemento > 5:
            print(f"Na lista 1, na posição {i}: {elemento}")
    for i, elemento in enumerate(lista2):
        if elemento > 5:
            print(f"Na lista 2, na posição {i}: {elemento}")
    for i, elemento in enumerate(lista3):
        if elemento > 5:
            print(f"Na lista 3, na posição {i}: {elemento}")

    # b) Números com mesmo índice que somam 15
    print("Índices com números que somam 15:")
    for i in range(tamanho):
        if lista1[i] + lista2[i] + lista3[i] == 15:
            print(f"Índice {i} possui números que somam 15")

    # c) Números de 0 a 9 presentes nas três listas
    numeros_presentes = []
    for numero in range(10):
        if numero in lista1 and numero in lista2 and numero in lista3:
            numeros_presentes.append(numero)
    print("Números de 0 a 9 presentes nas três listas:", numeros_presentes)
