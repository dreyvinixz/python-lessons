# Solicita a quantidade de alunos na turma
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

# Inicializa as listas
numeros_matricula = []
notas_alunos = []

# Preenche as listas com as informações dos alunos
for i in range(quantidade_alunos):
    matricula = input(f"Digite o número de matrícula do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    
    numeros_matricula.append(matricula)
    notas_alunos.append(nota)

# Calcula a média aritmética das notas
media_notas = sum(notas_alunos) / quantidade_alunos

# Mostra os números de matrícula dos alunos abaixo da média
print("\nAlunos abaixo da média:")
for i in range(quantidade_alunos):
    if notas_alunos[i] < media_notas:
        print(f"Número de Matrícula: {numeros_matricula[i]}")

print(f"\nMédia aritmética das notas: {media_notas:.2f}")
