class Nodo:

    def __init__(self,data):
        self.izq = None
        self.der = None
        self.data = data
    
    def insertar(self,data):
        if self.data:
            if data < self.data:
                if self.izq is None:
                    self.izq = Nodo(data)
                else:
                    self.izq.insertar(data)
            elif data > self.data:
                if self.der is None:
                    self.der = Nodo(data)
                else:
                    self.der.insertar(data)
        else:
            self.data = data
    
    def encontrarValor(self, valor):
        if valor < self.data:
            if self.izq is None:
                return 'EL VALOR NO FUE ENCONTRADO'
            return self.izq.encontrarValor(valor)
        elif valor > self.data:
            if self.der is None:
                return 'EL VALOR NO FUE ENCONTRADO'
            return self.der.encontrarValor(valor)
        else:
            return 'EL VALOR FUE ENCONTRADO'
    
    # Recorrido INORDEN: IZQUIERDA -> RAIZ -> DERECHA
    def inorden(self, root):
        res = []
        if root: 
            res = self.inorden(root.izq)
            res.append(root.data)
            res = res + self.inorden(root.der) 
        return res   

    # Recorrido PREORDEN: RAIZ -> IZQUIERDA -> DERECHA
    def preorden(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorden(root.izq)
            res = res + self.preorden(root.der)
        return res
        
    # Recorrido POSTORDEN: IZQUIERDA -> DERECHA -> RAIZ
    def postorden(self, root):
        res = []
        if root:
            res = self.postorden(root.izq)
            res = res + self.postorden(root.der)
            res.append(root.data)
        return res
    
    def printTree(self):
        if self.izq:
            self.izq.printTree()
        print(self.data)
        if self.der:
            self.der.printTree()


root = Nodo(10)
root.insertar(5)
root.insertar(20)
root.insertar(15)
root.insertar(3)
root.insertar(11)
root.insertar(90)
root.insertar(55)
root.insertar(2)
root.insertar(1)
root.insertar(4)

print(root.preorden(root))
print(root.postorden(root))
print(root.inorden(root))

# print(root.encontrarValor(3))
# print(root.encontrarValor(34))

# root.printTree()
