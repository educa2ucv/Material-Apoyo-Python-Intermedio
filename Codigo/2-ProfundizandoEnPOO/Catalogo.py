"""
    Ejercicio #01: 
        Desarrolle una clase Pelicula el cual contenga los atributos
        titulo, categoria y lanzamiento. Luego, desarrolle una clase 
        Catalogo que tenga por atributo un catalago de peliculas 
        y un método que nos permite obtener todas las películas
        correspondientes a una categoría indicada.

"""

class Pelicula:
    def __init__(self,titulo,categoria, lanzamiento):
        self.titulo = titulo
        self.categoria = categoria
        self.lanzamiento = lanzamiento

class Catalogo:

    def __init__(self,peliculas = []):
        self.peliculas = peliculas

    def filtrarCategoria(self,categoria):
        return filter ( lambda pelicula: pelicula.categoria == categoria, self.peliculas)

pelicula1 = Pelicula('Narnia', 'fantasia', '28/01/2021')
pelicula2 = Pelicula('Dragon Ball Z', 'anime', '28/01/2021')
pelicula3 = Pelicula('The Last', 'anime', '28/01/2021')
pelicula4 = Pelicula('Una casa patas arriba', 'comedia', '28/01/2021')
pelicula5 = Pelicula('La Batalla de los dioses', 'anime', '28/01/2021')
pelicula6 = Pelicula('Marley y yo', 'comedia', '28/01/2021')
pelicula7 = Pelicula('Piratas del Caribe', 'infantil', '28/01/2021')

peliculas = [pelicula1, pelicula2, pelicula3, pelicula4, pelicula5, pelicula6, pelicula7]

catalogo = Catalogo(peliculas)
resultados = catalogo.filtrarCategoria('anime')

for resultado in resultados:
    print(resultado.titulo)