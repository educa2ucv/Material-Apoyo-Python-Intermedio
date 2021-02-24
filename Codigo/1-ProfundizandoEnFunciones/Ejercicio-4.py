"""
    Ejercicio #04:
        Realice una función recursiva que calcule el número Fibonacci N-ésimo.
        La secuencia de Fibonacci viene definida de la siguiente manera:
           0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,…
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return ( fibonacci(n-1) + fibonacci(n-2) )
    
for i in range(101):
    print(fibonacci(i), end= " ")