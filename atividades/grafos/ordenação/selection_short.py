def selection_sort(arr):
    print("Execução do Selection Sort:")
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"Iteração {i + 1}:")
        print(f"  Antes: {arr}")
        # Encontrar o menor elemento no restante do vetor
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Trocar o menor elemento encontrado com o elemento atual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"  Depois: {arr}")
    print("Resultado Final:", arr)
    print("-" * 50)


# Vetores fornecidos
U = [1, 2, 3, 4, 5, 6]
V = [6, 5, 4, 3, 2, 1]

# Executando o Selection Sort
print("Para o vetor U=[1, 2, 3, 4, 5, 6]:")
selection_sort(U.copy())

print("Para o vetor V=[6, 5, 4, 3, 2, 1]:")
selection_sort(V.copy())