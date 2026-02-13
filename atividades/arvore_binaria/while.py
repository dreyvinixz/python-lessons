class TAD: 
    def __init__(self, tamanho): 
        self.vetor = [None] * tamanho 
        self.lim = tamanho - 1 
        self.base = 0 
        self.topo = self.base - 1 
    def M1(self): 
        if (self.topo >= self.base): 
            return self.vetor[self.topo] 
    def M2(self, dado): 
        if (self.topo < self.lim): 
            self.topo += 1 
            self.vetor[self.topo] = dado 
    def M3(self): 
        if (self.topo >= self.base): 
            self.topo -= 1 
 
obj = TAD(5)  
for i in range(5): 
    obj.M2(3*i) 
print(obj.vetor)
while i >= 3: 
    obj.M3() 
    i = i/2 
print(obj.M1())