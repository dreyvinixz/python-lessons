def troca(var):
    aux = var[0]
    var[0] = var[1]
    var[1] = aux

a = 10
b = 20
variaveis = [a, b]

print("1o print", "Valor de a:", a, "Valor de b:", b)
troca(variaveis)
print("2o print", "Valor de a:", variaveis[0], "Valor de b:", variaveis[1])

def imparesMenores(x):
    return [i for i in range(1, x + 1) if i % 2 != 0]


resultado = imparesMenores(8)
print(resultado)


def Resto(a, b):
    while a >= b:
        a -= b
    return a

resultado = Resto(10, 3)
print(resultado)

def interseccao(lista1, lista2):
    result = []
    for item in lista1:
        if item in lista2 and item not in result:
            result.append(item)
    return result

lista1 = [5, 4, 3, 5, 3, 4, 7, 3, 1]
lista2 = [5, 7, 3, 6, 8, 7, 5, 1, 3, 9]
resultado = interseccao(lista1, lista2)
print(resultado)
