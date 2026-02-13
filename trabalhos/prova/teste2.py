def num_pefct (numero):
    if numero <= 0:
        return False

    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma    += 1
    return soma == numero

entrada = int(input("difigite "))
if num_pefct(entrada ):
    print("a")
else:
    print("b")