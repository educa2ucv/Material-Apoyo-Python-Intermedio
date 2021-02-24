"""
    Ejercicio #01: 
        Realice un programa que lea un archivo cuyo nombre es
        "DataBase.txt", el cual contendrá por línea, el nombre de una persona
        su edad y su país de procedencia. Dicho programa debe generar un nuevo 
        archivo por CADA PAÍS presente en DataBase.txt donde únicamente se incluirá
        el nombre y edad de cada persona que corresponda con el país a almacenar en el archivo.
"""

def writeFile(nombre,edad,pais):
    pais = pais[:len(pais)-1]
    archivoAux = open( f'{pais}.txt', 'a' )
    archivoAux.write(f'{nombre} {edad}\n')
    archivoAux.close()

archivo = open('DataBase.txt')
paises = []

for linea in archivo:

    linea = linea.split(' ')
    nombre = linea[0]
    edad = linea[1]
    pais = linea[2]

    if not pais in paises:
        paises.append(pais)
        writeFile(nombre,edad,pais)
    else:
        writeFile(nombre,edad,pais)

archivo.close()

