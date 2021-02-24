def matCuadrado(n):

    matrix = []

    for i in range(n):
        matrix.append( [0]*n )

    return matrix

resultado = matCuadrado(10)

for i in range(10):
    for j in range(10):
        print(resultado[i][j], end=" ")
    print()

# for i in matrix:
#     print(i)