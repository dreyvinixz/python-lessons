import matplotlib.pyplot as plt
import time

# Função de merge
def merge(arr, left, mid, right):
    n1 = mid - left + 1  # Tamanho do subvetor esquerdo
    n2 = right - mid     # Tamanho do subvetor direito

    # Criar os dois subvetores
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    # Combinação dos subvetores
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar os elementos restantes do subvetor esquerdo
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar os elementos restantes do subvetor direito
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Função recursiva Merge Sort
def merge_sort(arr, left, right, step=0):
    if left < right:
        mid = (left + right) // 2

        # Etapa de divisão do vetor
        print(f"Etapa {step}: Dividindo {arr[left:right+1]}")
        visualize(arr, left, mid, right, step, "Dividindo")

        merge_sort(arr, left, mid, step + 1)    # Parte esquerda
        merge_sort(arr, mid + 1, right, step + 1)  # Parte direita

        # Etapa de combinação dos vetores
        merge(arr, left, mid, right)
        print(f"Etapa {step}: Combinando {arr[left:right+1]}")
        visualize(arr, left, mid, right, step, "Combinando")

# Função para visualizar o vetor graficamente
def visualize(arr, left, mid, right, step, action):
    plt.figure(figsize=(10, 6))
    plt.title(f"Etapa {step} - {action}")
    plt.bar(range(len(arr)), arr, color=['gray' if left <= i <= right else 'lightblue' for i in range(len(arr))])
    plt.xlabel("Índices")
    plt.ylabel("Valores")
    plt.show()
    time.sleep(0.5)  # Pausa para visualização

# Vetor fornecido
A = [3, 41, 52, 26, 38, 57, 9, 49]

print("Vetor Original:", A)
merge_sort(A, 0, len(A) - 1)
print("Vetor Ordenado:", A)
