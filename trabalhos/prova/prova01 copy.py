class SistemaCashback:
    def __init__(self):
        # Dicionário para armazenar empresas e seus respectivos descontos
        self.empresas = {"ALB": 10, "MM": 8, "CZB": 5}

        # Dicionário para armazenar usuários e seus saldos
        self.usuarios = {}

    def cadastrar_empresa(self):
        id_empresa = input("Digite o ID da empresa: ").upper()
        if id_empresa not in self.empresas:
            desconto = float(input("Digite a porcentagem de cashback oferecida pela empresa: "))
            self.empresas[id_empresa] = desconto
            print(f"Empresa {id_empresa} cadastrada com sucesso.")
        else:
            print("Empresa já cadastrada.")

    def cadastrar_usuario(self):
        id_usuario = input("Digite o ID do usuário: ").upper()
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = 0.0
            print(f"Usuário {id_usuario} cadastrado com sucesso.")
        else:
            print("Usuário já cadastrado.")

    def registrar_compra(self):
        id_usuario = input("Digite o ID do usuário: ").upper()
        if id_usuario not in self.usuarios:
            print("Usuário não cadastrado.")
            return

        valor_compra = float(input("Digite o valor da compra: "))
        id_empresa = input("Digite o ID do local da compra: ").upper()
        if id_empresa not in self.empresas:
            print("Empresa não cadastrada.")
            return

        desconto = self.empresas[id_empresa]
        valor_desconto = (desconto / 100) * valor_compra

        self.usuarios[id_usuario] += valor_desconto
        print(f"Compra registrada com sucesso. Cashback de R$ {valor_desconto:.2f} adicionado ao saldo do usuário.")

    def mostrar_saldo(self):
        id_usuario = input("Digite o ID do usuário: ").upper()
        if id_usuario in self.usuarios:
            saldo = self.usuarios[id_usuario]
            print(f"Saldo do usuário {id_usuario}: R$ {saldo:.2f}")
        else:
            print("Usuário não cadastrado.")

    def resgatar_saldo(self):
        id_usuario = input("Digite o ID do usuário: ").upper()
        if id_usuario in self.usuarios:
            saldo = self.usuarios[id_usuario]
            print(f"Saldo atual do usuário {id_usuario}: R$ {saldo:.2f}")

            confirmacao = input("Deseja mesmo resgatar o saldo? (Sim/Não): ").lower()
            if confirmacao == "sim":
                print(f"Dinheiro transferido. Saldo do usuário {id_usuario} atualizado para R$ 0.00.")
                self.usuarios[id_usuario] = 0.0
            else:
                print("Resgate cancelado.")
        else:
            print("Usuário não cadastrado.")

    def excluir_empresa(self):
        id_empresa = input("Digite o ID da empresa a ser excluída: ").upper()
        if id_empresa in self.empresas:
            confirmacao = input(f"Deseja mesmo excluir a empresa {id_empresa}? (Sim/Não): ").lower()
            if confirmacao == "sim":
                del self.empresas[id_empresa]
                print(f"Empresa {id_empresa} excluída com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Empresa não cadastrada.")


# Instanciando o sistema
sistema_cashback = SistemaCashback()

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Empresa")
    print("2 - Cadastrar Usuário")
    print("3 - Registrar Compra de um Usuário")
    print("4 - Mostrar Saldo de um Usuário")
    print("5 - Resgatar Saldo de um Usuário")
    print("6 - Excluir Empresa")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        sistema_cashback.cadastrar_empresa()
    elif opcao == "2":
        sistema_cashback.cadastrar_usuario()
    elif opcao == "3":
        sistema_cashback.registrar_compra()
    elif opcao == "4":
        sistema_cashback.mostrar_saldo()
    elif opcao == "5":
        sistema_cashback.resgatar_saldo()
    elif opcao == "6":
        sistema_cashback.excluir_empresa()
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
