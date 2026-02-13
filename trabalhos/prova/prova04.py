def ler_lista(): # defino uma função 
    lista = [] # defino uma lista
    while True: # se o loop for verdade
        try:
            numero = int(input("Digite um número (0 para encerrar): ")) # pesso uma entrda
            if numero == 0: # se a entrda for == 0
                break # pulo
            lista.append(numero) # prencheo a lista com a entrda
        except ValueError:
            print("Erro: Digite um valor válido.")

    return lista # retorno a lista

def encontrar_elementos_comuns(lista1, lista2): # defino uma funlçao 2 com 2 paramentros 
    elementos_comuns = set(lista1) & set(lista2) # verifico o elemnto em comum das duas listas 
    return list(elementos_comuns) # retoo o elemento em comum

# Ler as duas listas
print("Para a primeira lista:")
lista1 = ler_lista() 

print("\nPara a segunda lista:")
lista2 = ler_lista()

# Encontrar elementos comuns
elementos_comuns = encontrar_elementos_comuns(lista1, lista2) 

# Mostrar resultados
if elementos_comuns:
    print(f"\nElementos comuns encontrados: {elementos_comuns}")
else:
    print("\nNão foram encontrados elementos comuns.")
