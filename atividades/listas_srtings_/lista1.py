num_matriculas = []    #lista vazia usada depois para colocar o dados de entrada do usuario do numero de matricula
notas = []  #lista vazia usada depois para colocar o dados de entrada do usuario das notas
#estrutura de repetição
while True:
    try: #coverte para inteiro
        quantidade_alunos = int(input("digite uma quantidade de alunos: ")) #recebe a quantidade de alunos
        if quantidade_alunos <= 0:  #se a quantidade de alunos for menor ou igual a 0
            print("A quantidade de alunos deve ser maior que 0")  #imprimo que deve ser maior que 0
        else:  #caso a quantidade de alunos seja maior
            for i in range(quantidade_alunos):  #entro no meu laço de repetição n vezes, sendo n a quantidade de alunos insirida pelo usuario 
                matriculas = int(input("digite o numero de matricula: "))   #dentro do laço peço um numero de matricula para o aluno
                nota = float(input("digite a nota do aluno {} : ".format(matriculas)))  #tambem peço uma nota
                num_matriculas.append(matriculas) #guardo o numero de matricula dentro da lista vazia
                notas.append(nota) #faço o mesmo para a nota
            break
    except ValueError: #exeção para o erro de tentativa de conversão
        print("Por Favor, digite um numero racional postivo e > 0") #caso a entrada seja um numero que não atende os requesitos imprimo*

#media aritimetica

media = sum(notas) / quantidade_alunos #calculo a media aritimetica e uso sum para somar as notas dos alunos
print("Media Aritimetica: soma das nota / quantidade de alunos =",media) #imprimo como calcular media aritimetica e mostro ela
#alunos abaixo da media

print("Alunos abaixo da media:") #irei mostrar os alunos com nota abaixo da media
alunos_abaixo_da_media = False #de inicio não havera alunos com nota abaixo da media
for i in range(quantidade_alunos): #laço de repetição usado para verificar se há alunos com nota baixa
    if notas[i] < media: #pecorro a lista de quantidade de alunos e verifico se tem alunos com notas abaixo da media
        print(num_matriculas[i]) #caso há alunos com nota inferior imprimo seu numero de matricula
        alunos_abaixo_da_media = True #varivel caso haja um aluno com nota menor que a media e definida como true

if not alunos_abaixo_da_media: #condiçional que verifica se não há alunos com notas inferior a media
    print("não há alunos abaixo da media") #imprimo que não a alunos abaixo da media
