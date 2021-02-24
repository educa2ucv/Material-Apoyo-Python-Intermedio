def factorial(n):
    # Caso Base
    if n == 1:
        return 1
    # Caso Recursivo
    else:
        return n * factorial( n-1 )
    
def fact_iterativo(n):
    acumulador = 1
    for i in range(1,n+1):
        acumulador *= i
    return acumulador

# print( fact_iterativo(5) )
# print( fact_iterativo(10) )
# print( fact_iterativo(100) )

# print( factorial(5) )
# print( factorial(10) )
# print( factorial(100) )

def es_potencia(n,b,exp):
    if n == (b**exp):
        return True
    elif (b**exp) > n:
        return False
    else:
        return es_potencia(n,b,exp+1)

def es_potencia_iterativo(n,b):
    for exp in range(0,n+1):
        if (b**exp) == n:
            return True
        elif (b**exp) > n:
            return False 

def triangular(n,acum,i):
    if i == n:
        return acum+i
    else:
        return triangular(n,acum+i,i+1)

def triangular_iterativo(n):
    acum = 0
    for i in range(1,n+1):
        acum += i
    return acum

print(triangular_iterativo(5))
print(triangular_iterativo(10))

# print(es_potencia_iterativo(8,2))
# print(es_potencia_iterativo(64,4))
# print(es_potencia_iterativo(70,10))

# print(es_potencia(8,2,0))        
# print(es_potencia(64,4,0))        
# print(es_potencia(70,10,0))        