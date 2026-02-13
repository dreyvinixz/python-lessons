# Definição das listas
x = [4, 1, 6, 8, 6, 2, 7]
y = [8, 6, 5, 3, 0, 9, 1]
z = [5, 1, 4, 2, 8, 1, 3]

# a) Números maiores que 5 e suas posições
print("\na) Números maiores que 5:")
for lista, numeros in zip(['x', 'y', 'z'], [x, y, z]):
    for i, num in enumerate(numeros):
        if num > 5:
            print(f"Número {num} na lista {lista}, posição {i}")

# b) Índices com números que somam exatamente 15
print("\nb) Índices com números que somam exatamente 15:")
for i in range(len(x)):
    if x[i] + y[i] + z[i] == 15:
        print(f"Índice {i}")

# c) Números de 0 a 9 presentes nas três listas
print("\nc) Números de 0 a 9 presentes nas três listas:")
for num in range(10):
    if num in x and num in y and num in z:
        print(f"Número {num} presente nas três listas.")
