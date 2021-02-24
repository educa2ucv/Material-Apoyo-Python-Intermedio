class Persona:

    def __init__(self,nombre,edad,nacionalidad):  
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def comer(self):
        print('Estoy comiendo')
    def dormir(self):
        print('Estoy durmiendo')
    def programando(self):
        print('Estoy programando')

objeto1 = Persona('Alexanyer',22,'Venezolano')
objeto2 = Persona('Elizabeth',15,'Española')

objeto1.comer()
objeto2.programando()