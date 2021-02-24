"""
    Ejercicio #02: Tomando los archivos generados del ejercicio anterior, 
    genera un nuevo archivo cuyo nombre será "Mayores.txt" donde 
    únicamente se encuentre el nombre y edad de la persona con 
    mayor edad entre todas pertenecientes a su país.
    El formato de salida del archivo tiene que ser el siguiente:

    Nombre_Pais:
    Nombre_Persona Edad
    Nombre_Pais:
    Nombre_Persona Edad
    Nombre_Pais:
    Nombre_Persona Edad
"""

from Main import paises

def maxiEdad(file):

    mayorEdad = 0
    nombreMayorEdad = ''

    for line in file:
        line = line.split(' ')
        nombreMayorEdad = line[0]
        edad = int(line[1])

        if edad >= mayorEdad:
            mayorEdad = edad

    return mayorEdad, nombreMayorEdad

def readFile():

    mayores = open('Mayores.txt', 'w')

    for pais in paises:
        pais = pais[:len(pais)-1]

        aux = open(f'{pais}.txt')
        result = maxiEdad(aux)
        aux.close()

        mayores.write(f'{pais}:\n{result[1]} {result[0]}\n')

    mayores.close()

readFile()