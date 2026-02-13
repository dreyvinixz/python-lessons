# Verificação do email
while True:
    email = input("Digite o email: ")
    if "@" in email:
        print("Email válido!")
    else:
        print("Email inválido!")
