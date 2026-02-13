# Lista de produtos
produtos = {
    10: {"nome": "Caderno pautado", "preco": 10.00},
    20: {"nome": "Caneta azul", "preco": 3.00},
    21: {"nome": "Caneta vermelha", "preco": 3.00},
    30: {"nome": "Borracha", "preco": 2.00},
    45: {"nome": "Lápis macio", "preco": 1.00}
}

# Lista para armazenar o pedido do cliente
pedido_cliente = []

# Variável para acumular o valor total do pedido
valor_total = 0.0

# Solicita o nome do cliente
nome_cliente = input("Digite o nome do cliente: ")

# Loop para receber os códigos e quantidades dos produtos
while True:
    # Mostra o menu de produtos
    print("\nMenu de Produtos:")
    for codigo, produto in produtos.items():
        print(f"{codigo} {produto['nome']} R$ {produto['preco']:.2f}")

    # Solicita código do produto e quantidade
    codigo_produto = int(input("Digite o código do produto (0 para encerrar): "))
    
    # Verifica se o código é 0 para encerrar o pedido
    if codigo_produto == 0:
        break

    # Verifica se o código do produto é válido
    if codigo_produto not in produtos:
        print("Código de produto inválido. Tente novamente.")
        continue

    quantidade = int(input(f"Digite a quantidade de '{produtos[codigo_produto]['nome']}': "))

    # Verifica se a quantidade é um número inteiro positivo
    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue

    # Adiciona o produto e a quantidade ao pedido do cliente
    pedido_cliente.append((codigo_produto, quantidade))

    # Atualiza o valor total do pedido
    valor_total += produtos[codigo_produto]['preco'] * quantidade

# Imprime o resumo do pedido
print(f"\nCliente: {nome_cliente}")
for codigo, quantidade in pedido_cliente:
    produto = produtos[codigo]
    subtotal = produto['preco'] * quantidade
    print(f"{subtotal:.2f} {quantidade} x {produto['nome']}")

# Imprime o valor total
print("-----------")
print(f"{valor_total:.2f} valor total")
