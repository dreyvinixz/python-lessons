#boa noite professor, este e meu projeto que foi pedido, dei o nome do arquivo como main , 
# não estava na aula então não sei se era para salvar de outra forma 
# no meio do processo tive algumas duvidas e recorri a meios alternativos não falados em aula, 
# mas que são do meu conhecimento, as duvidas tirarei na aula.

#lista dos produtos
produtos = [
    [10, "Caderno pautado", 10.00],
    [20, "Caneta azul", 3.00],
    [21, "Caneta vermelha", 3.00],
    [30, "Borracha", 2.00],
    [45, "Lápis macio", 1.00]
] 
#apresentação dos menus
print("Seja bem vindo a nossa loja\nMenu de produtos:") 
print('10:','Caderno azul', '- R$ 10.00' )
print('20:','Caneta azul', '- R$ 3.00')
print('21:','caneta vermelha', '- R$ 3.00')
print('30:','Borracha', '- R$ 2.00')
print('45:','Lápis macio', '- R$ 1.00')

nome_cliente = input("Digite seu nome: ") #entrada para receber o nome do cliente  
cods_order = [] # Lista para armazenar os códigos dos produtos
quantidade_order = [] # Lista para armazenar as quantidades de cada produto

cod = -1
while cod != 0: #loop
    try: #try e usaso para capturar possíveis exceções e lidar com elas de forma adequada.
        cod = int(input("Digite o código do produto ou 0 para sair: "))

        if cod != 0: #condição
            # Verifica se o código do produto é válido
            produto_encontrado = False
            i = 0
            while i < len(produtos) and not produto_encontrado:
                if produtos[i][0] == cod:
                    produto_encontrado = True
                i = i + 1

            if produto_encontrado:
                # Solicita a quantidade do produto e registra o código e quantidade
                quantidade = int(input("Digite a quantidade: ")) #entrada para quantidade de produtos comprados 
                cods_order.append(cod) 
                quantidade_order.append(quantidade)

            if not produto_encontrado:
                print("Código inválido. Tente novamente.")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Cálculo do valor total do pedido e criação do resumo da compra
valor_total = 0.0
resumo_compra = "" # Inicializa a variável resumo_compra como uma string vazia

i = 0
while i < len(cods_order):
    cod = cods_order[i]
    quantidade = quantidade_order[i]

    produto_encontrado = False
    j = 0
    while j < len(produtos) and not produto_encontrado:
        if produtos[j][0] == cod:
            produto_encontrado = True
            preco_unitario = produtos[j][2]
            nome_produto = produtos[j][1]
            valor_item = preco_unitario * quantidade
            valor_total = valor_total + valor_item
            resumo_compra = resumo_compra + str('R$ {}'.format(valor_item)) + " " + str(quantidade) + " x " + nome_produto + "\n"
        j = j + 1

    if not produto_encontrado:
        print("Produto com código {} não encontrado.".format(cod))
    i = i + 1

# Exibição do resumo da compra
if resumo_compra:
    print("Resumo da compra:")
    print("Cliente:", nome_cliente)
    print(resumo_compra)
    print("-----------")
    print("valor total: R$ {}".format(valor_total))
else:
    print("Obrigado por utilizar nosso sistema!")
