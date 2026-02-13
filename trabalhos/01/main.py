# Lista de empresas pré-cadastradas
empresas = [
    ["ALB", 10], 
    ["MM", 8], 
    ["CZB", 5]
]

# Lista de usuários cadastrados
usuarios = []

# Exibir o menu
print("Bem-vindo ao nosso sistema!\nSelecione a opção desejada: ")
print("1 - Cadastrar Empresa")
print("2 - Cadastrar Usuário")
print("3 - Registrar Compra de Usuário")
print("4 - Mostrar Saldo de Usuário")
print("5 - Resgatar Saldo de Usuário")
print("6 - Excluir Empresa")
print("0 - Para sair do programa")

while True:
    try:
        # Recebe a entrada do usuário e converte para inteiro
        select_option = int(input("Digite o número da opção desejada: "))

        if select_option == 0:
            print("Obrigado por usar nosso sistema.")
        elif select_option == 1:
            print("opção 1 selecionada!")
            # Exibir opções de empresas e cashbacks
            print("Opções de Empresas e Cashbacks:")
            for empresa in empresas:
               print("Empresa:", empresa[0], "| Cashback:", empresa[1], "%")
            # Cadastrar Empresa
            id_empresa = input("Digite o ID da empresa: ")
            cashback = float(input("Digite a porcentagem de cashback oferecida pela empresa(inteiro): "))

            # Verifica se a empresa já está cadastrada 
            for empresa in empresas:
                if id_empresa == empresa[0]:
                    print("Empresa cadastrada.")
                    break
            else:
                # Adicionar a nova empresa à lista de empresas
                empresas.append([id_empresa, cashback])
                print("Empresa cadastrada com sucesso.")

        elif select_option == 2:
            print("opção 2 selecionada!")
            # Cadastrar Usuário
            id_usuario = input("Digite o ID do usuário(numero de matricula): ")
            saldo = 0.0

            # Verificar se o usuário já está cadastrado
            for usuario in usuarios:
                if id_usuario == usuario[0]:
                    print("Usuário já cadastrado.")
                    break
            else:
                # Adicionar o novo usuário à lista de usuários
                usuarios.append([id_usuario, saldo])
                print("Usuário cadastrado com sucesso.")
        
        elif select_option == 3:
            print("opção 3 selecionada!")
            # Registrar Compra de Usuário
            id_usuario = input("Digite o ID do usuário(numero de matricula): ")
            valor_compra = float(input("Digite o valor da compra: "))
            id_empresa = input("Digite o ID da empresa: ")
            
            # Verificar se o usuário está cadastrado
            for usuario in usuarios:
                if id_usuario == usuario[0]:
                    # Verificar se a empresa está cadastrada
                    for empresa in empresas:
                        if id_empresa == empresa[0]:
                            # Calcular o valor do cashback
                            cashback = (empresa[1] / 100) * valor_compra
                            # Atualizar o saldo do usuário
                            usuario[1] += cashback
                            print("Compra registrada com sucesso.")
                            break
                    else:
                        print("Empresa não cadastrada.")
                    break
            else:
                print("Usuário não cadastrado.")
        
        elif select_option == 4:
            print("opção 4 selecionada!")
            # Mostrar Saldo de Usuário
            id_usuario = input("Digite o ID do usuário(numero de matricula): ")
            
            # Verificar se o usuário está cadastrado
            for usuario in usuarios:
                if id_usuario == usuario[0]:
                    print("INFORMAÇÕES DE COMPRA | \nEmpresa Cadastrada: {} \nValor depositado: {}".format(id_empresa,valor_compra))
                    print("Saldo do usuário", id_usuario + ":", "R$", format(usuario[1], ".2f"))
                    break
            else:
                print("Usuário não cadastrado.")
            
        elif select_option == 5:
            print("opção 5 selecionada!")
            # Resgatar Saldo de Usuário
            id_usuario = input("Digite o ID do usuário(numero de matricula): ")
            
            # Verificar se o usuário está cadastrado
            for usuario in usuarios:
                if id_usuario == usuario[0]:
                    print("Saldo atual do usuário", id_usuario + ":", "R$", format(usuario[1], ".2f"))
                    confirmacao = input("Deseja mesmo resgatar o saldo? (Sim/Não): ")
                    if confirmacao.lower() == "sim":
                        usuario[1] = 0.0
                        print("Saldo resgatado com sucesso.")
                    break
            else:
                print("Usuário não cadastrado.")
        
        elif select_option == 6:
            print("opção 6 selecionada!")
            # Excluir Empresa
            id_empresa = input("Digite o ID da empresa: ")
            
            # Verificar se a empresa está cadastrada
            for empresa in empresas:
                if id_empresa == empresa[0]:
                    confirmacao = input(f"Deseja mesmo excluir a empresa {id_empresa}? (Sim/Não): ")
                    if confirmacao.lower() == "sim":
                        empresas.remove(empresa)
                        print("Empresa excluída com sucesso.")
                    break
            else:
                print("Empresa não cadastrada.")
        
        else:
            print("Opção inválida. Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correto.")
