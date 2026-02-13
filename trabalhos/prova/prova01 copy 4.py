# Inicialização das variáveis
total_homens = 0
total_mulheres = 0
soma_peso_homem = 0
soma_peso_mulher = 0

# Leitura das informações sobre o grupo
for _ in range(5):
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    sexo = input("Digite o sexo da pessoa (F/M): ").upper()

    if sexo == 'M':
        total_homens += 1
        soma_peso_homem += peso
    elif sexo == 'F':
        total_mulheres += 1
        soma_peso_mulher += peso

# Cálculo dos dados estatísticos
percentual_mulheres = (total_mulheres / 5) * 100
percentual_homens = (total_homens / 5) * 100
media_peso_mulher = soma_peso_mulher / total_mulheres if total_mulheres > 0 else 0
media_peso_homem = soma_peso_homem / total_homens if total_homens > 0 else 0

# Exibição dos resultados
print(f"\nQuantidade total de homens: {total_homens}")
print(f"Quantidade total de mulheres: {total_mulheres}")
print(f"Percentual de homens: {percentual_homens:.1f}%")
print(f"Percentual de mulheres: {percentual_mulheres:.1f}%")
print(f"Média de peso das mulheres: {media_peso_mulher:.2f}")
print(f"Média de peso dos homens: {media_peso_homem:.2f}")
