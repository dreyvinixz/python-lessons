from graphviz import Digraph

# Criando o objeto Digraph
dot = Digraph()

# Adicionando os estados
dot.node('q0', 'q0', shape='circle')  # Estado inicial (S)
dot.node('q1', 'q1', shape='circle')  # Estado intermediário após ler "a" (parte de S -> abA)
dot.node('q2', 'q2', shape='circle')  # Estado intermediário A
dot.node('q3', 'q3', shape='circle')  # Estado intermediário após ler "b" (parte de A -> baB)
dot.node('q4', 'q4', shape='circle')  # Estado intermediário B
dot.node('q5', 'q5', shape='circle')  # Estado intermediário após ler o primeiro "b" de B -> bb
dot.node('q6', 'q6', shape='doublecircle')  # Estado final após ler o segundo "b" (final para B -> bb)

# Adicionando transições
# Transições para S -> abA
dot.edge('q0', 'q1', label='a')    # q0 -> q1 ao ler "a"
dot.edge('q1', 'q2', label='b')    # q1 -> q2 ao ler "b"

# Transições para A -> baB
dot.edge('q2', 'q3', label='b')    # q2 -> q3 ao ler "b"
dot.edge('q3', 'q4', label='a')    # q3 -> q4 ao ler "a"

# Transições para B -> aA
dot.edge('q4', 'q2', label='a')    # q4 -> q2 ao ler "a" (retorna ao estado A)

# Transições para B -> bb
dot.edge('q4', 'q5', label='b')    # q4 -> q5 ao ler "b"
dot.edge('q5', 'q6', label='b')    # q5 -> q6 ao ler "b" (estado final)

# Definindo o estado inicial com cor azul
dot.node('q0', color='blue')

# Renderizando e salvando o gráfico
dot.render('afn_grammar', format='png', cleanup=True)
