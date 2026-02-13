#Prova
#164402 - Andrey Vinicius Santos Souza 

from multiprocessing.sharedctypes import Value

list = []
print("bem vindo ao nosso sistema!")
valor_diario = 0
try:
    if valor_diario >= 0:
        for s in range(1,8):
            a = int(input(("Digite o valor das ações do dia {}: ".format(s))))
            list.append(a)
except ValueError:
    print("digite um numero inteiro")

#media 
media = sum(list) / 7
print("A media dos dias das ações foram:",media)

# dias 
x = print("dia 1, Valor da ação = {}".format(list[0]))
x1 = print("dia 2, Valor da ação = {}".format(list[1]))
x2 = print("dia 3, Valor da ação = {}".format(list[2]))
x3 = print("dia 4, Valor da ação = {}".format(list[3]))
x4 = print("dia 5, Valor da ação = {}".format(list[4]))
x5 = print("dia 6, Valor da ação = {}".format(list[5]))
x6 = print("dia 7, Valor da ação = {}".format(list[6]))
