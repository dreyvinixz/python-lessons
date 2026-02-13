class Tree:
    def __init__(self, data):
        self.left = None
        self.info = data
        self.right = None

    # Métodos de percurso para a subárvore esquerda
    def imprimir_pre_left(self):
        print(self.info)
        if self.left:
            self.left.imprimir_pre_left()
        if self.right:
            self.right.imprimir_pre_left()

    def imprimir_in_left(self):
        if self.left:
            self.left.imprimir_in_left()
        print(self.info)
        if self.right:
            self.right.imprimir_in_left()
    
    def imprimir_post_left(self):
        if self.left:
            self.left.imprimir_post_left()
        if self.right:
            self.right.imprimir_post_left()
        print(self.info)

    # Métodos de percurso para a subárvore direita
    def imprimir_pre_right(self):
        print(self.info)
        if self.right:
            self.right.imprimir_pre_right()
        if self.left:
            self.left.imprimir_pre_right()

    def imprimir_in_right(self):
        if self.right:
            self.right.imprimir_in_right()
        print(self.info)
        if self.left:
            self.left.imprimir_in_right()
    
    def imprimir_post_right(self):
        if self.right:
            self.right.imprimir_post_right()
        if self.left:
            self.left.imprimir_post_right()
        print(self.info)

    # Método para escolher o percurso
    def imprimir_metodo(self, lado, metodo):
        if lado == 'left':
            if metodo == 'pre':
                self.imprimir_pre_left()
            elif metodo == 'in':
                self.imprimir_in_left()
            elif metodo == 'post':
                self.imprimir_post_left()
        elif lado == 'right':
            if metodo == 'pre':
                self.imprimir_pre_right()
            elif metodo == 'in':
                self.imprimir_in_right()
            elif metodo == 'post':
                self.imprimir_post_right()
        else:
            print("Opção inválida!")

    def localizar(self, v):
        if v == self.info:
            return self
        if self.left:
            encontrado = self.left.localizar(v)
            if encontrado:
                return encontrado
        if self.right:
            encontrado = self.right.localizar(v)
            if encontrado:
                return encontrado
        return None  
    
    def inserir(self, main, secondary, lado):
        # Primeiro, localiza o nó principal onde será feita a inserção
        pai = self.localizar(main)
        
        if pai:
            if lado == 'left':
                if pai.left is None:
                    pai.left = Tree(secondary)
                    print(f"Nó '{secondary}' inserido à esquerda de '{main}'")
                else:
                    print(f"O nó '{main}' já possui um filho à esquerda")
            elif lado == 'right':
                if pai.right is None:
                    pai.right = Tree(secondary)
                    print(f"Nó '{secondary}' inserido à direita de '{main}'")
                else:
                    print(f"O nó '{main}' já possui um filho à direita")
            else:
                print("Lado inválido! Use 'left' ou 'right'.")
        else:
            print(f"Nó '{main}' não encontrado na árvore.")


# Definindo a árvore
raiz = Tree("A")
raiz.left = Tree("B")
raiz.right = Tree("C")
raiz.left.left = Tree("D")
raiz.left.right = Tree("E")

valor_procurado = "H"
nodo = raiz.localizar(valor_procurado)

if nodo:
    print(f"Nó encontrado: {nodo.info}")
else:
    print("Nó não encontrado")

# Entrada do usuário
lado = input("Escolha o lado ('left' ou 'right'): ").strip().lower()
metodo = input("Escolha o método ('pre', 'in' ou 'post'): ").strip().lower()

# Exibindo o percurso de acordo com a escolha do usuário
print("\nResultado do percurso escolhido:")
raiz.imprimir_metodo(lado, metodo)
