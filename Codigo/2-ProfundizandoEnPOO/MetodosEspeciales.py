"""
    Python nos ofreceme un conjunto de métodos especiales
    para la definición de clases. 

        Constructor: __init__
        Destructor: __del__
        Representación en String: __str__
        Longitud: __len__

"""
class Chocolate:

    def __init__(self,azucar,ingredientes):
        self.azucar = azucar
        self.ingredientes = ingredientes
    
    # def __del__(self):
    #     return f'Destruimos el objeto Chocolate'

    def __str__(self):
        return f'Soy un chocolate que tiene esta cantidad de azucar: {self.azucar}'

    def __len__(self):
        return len(self.ingredientes)

ejemplo = Chocolate(120.00, ['azucar', 'cacao', 'endulzantes'])
print(ejemplo.__str__())
print(ejemplo.__len__())