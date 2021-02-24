"""
    Ejercicio #01:
        Desarrolle una función que reciba una lista
        de asignaturas (Matemáticas, Fisica, Quimica, Historia y Lenguaje)
        pregunta al usuario la nota que ha sacado en cada una y elimine de la lista
        las asignaturas aprobadas. Al final, el programa debe mostrar
        por pantalla las asignaturas que el usuario tiene que repetir.
"""

asignaturas = [ 'Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lenguaje']

def foo(asignaturas:list) -> None:
    copia = asignaturas[:]
    for asig_actual in asignaturas:
        nota = int(input(f'Por favor, ingrese la nota de asignatura {asig_actual}: '))
        if nota >= 10:
            copia.remove(asig_actual)
    
    print(f'Las asignaturas a repetir son: {copia}')

#foo(asignaturas)

def foo2(n):
    n = n + 1000
    return n

numero = 1000
numero = foo2(numero)
print(numero)