class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
        
    def saludo(self):
        print('Hola desde el padre')

class Hija(Persona):

    def __init__(self,nombre):
        Persona.__init__(self,nombre)
    
    def saludo(self,nombre):
        print(f'Hola {nombre}')

class Hijo(Persona):

    def __init__(self,nombre):
        Persona.__init__(self,nombre)

    def saludo(self):
        print('Hola desde Hijo')

ejemplo = Hijo('Alexanyer')
ejemplo.saludo()