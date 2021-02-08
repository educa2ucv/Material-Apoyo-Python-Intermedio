archivo = open('Data.txt')

lineas = archivo.readlines()
auxiliar = []

for linea in lineas:

    if linea[::len(linea)-2] != '\0':
        linea = linea[:len(linea)-1]
    
    auxiliar.append(linea)

print(auxiliar)

# linea = archivo.readline()

# while linea != '':
#     print(linea)
#     linea = archivo.readline()

# for linea in archivo:
#     print(linea)