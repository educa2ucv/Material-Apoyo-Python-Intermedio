"""
    Ejercicio #02:
        Escribir una función que calcule recursivamente el n-ésimo
        número triangular (el número 1 + 2 + 3 + ... + n).
"""


def suma_recursiva(n,acum,i):
    if n == i:
        return (acum+i)
    else:
        return suma_recursiva(n,acum+i,i+1)

def suma_iterativa(n):
    acum = 0
    for j in range(1,n+1):
        acum += j
    return acum

print (suma_iterativa(3))
print (suma_iterativa(5))
print (suma_iterativa(10))
print (suma_iterativa(20))

# print( suma_recursiva(3,0,1) )
# print( suma_recursiva(5,0,1) )
# print( suma_recursiva(10,0,1) )
# print( suma_recursiva(20,0,1) )