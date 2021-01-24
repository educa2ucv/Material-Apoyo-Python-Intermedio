"""
    Ejercicio #03:
        Realice una función recursiva que indique si un número es potencia de otro.
        Por ejemplo:
            8 es potencia de 2
            64 es potencia de 8
            70 no es potencia de 10
            N es potencia de A
"""

def es_potencia(n,a,exp):
    # Caso Base 1
    if n == (a**exp):
        return True
    # Caso Base 2
    elif n < (a**exp):
        return False
    # Caso Recursivo
    else:
        return es_potencia(n,a,exp + 1)

def es_potencia_iterativo(n,a):
    for j in range(0,n+1):
        if (a**j) == n:
            return True
        elif n < (a**j):
            return False

print ( es_potencia_iterativo(8,2))
print ( es_potencia_iterativo(64,8))
print ( es_potencia_iterativo(70,10))
  
# print ( es_potencia(8,2,0))
# print ( es_potencia(64,8,0))
# print ( es_potencia(70,10,0))