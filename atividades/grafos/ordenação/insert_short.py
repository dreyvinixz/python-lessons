def insertion_sort(arr):
    print("Execução do Insertion Sort:")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Iteração {i}:")
        print(f"  Antes: {arr}")
        # Deslocar elementos maiores para frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"  Depois: {arr}")
    print("Resultado Final:", arr)
    print("-" * 50)

# Vetores fornecidos
U = [1, 2, 3, 4, 5, 6]
V = [6, 5, 4, 3, 2, 1]

# Executando o Insertion Sort
print("Para o vetor U=[1, 2, 3, 4, 5, 6]:")
insertion_sort(U.copy())

print("Para o vetor V=[6, 5, 4, 3, 2, 1]:")
insertion_sort(V.copy())