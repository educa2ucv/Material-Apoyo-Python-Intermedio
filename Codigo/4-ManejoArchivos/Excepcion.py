try:
    archivo = open('./Pepito.txt')
    print(archivo.readlines())
    archivo.close()
except:
    print('El archivo no ha sido encontrado :(')