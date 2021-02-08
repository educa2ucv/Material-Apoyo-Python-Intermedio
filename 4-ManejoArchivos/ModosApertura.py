"""
    La función open recibe un parámetro opcional para indicar
    el modo en que se abrirá el archivo. Los tres modos de apertura
    que se pueden especificar son:

        * Solo Lectura (r):  No se puede modificar el contenido del archivo
        solamente leer su contenido. 
        
        * Solo Escritura (w): En este caso, el archivo es truncado (vaciado)
        si existe, y se crea en caso contrario.

        * Modo Append (a): En este caso se crea el archivo, si no existe, pero 
        en caso de que exista se posiciona al final, manteniendo el contenido
        original. 

        Adicional: Se puede agregar un '+' para pasar a un modo
        lectura - escritura.
"""

# archivo = open('Ejemplo.txt', 'w')
# archivo.write('Hola Mundo\n')
# archivo.write('Hola Mundo\n')
# archivo.write('Hola Mundo\n')
# archivo.write('Hola Mundo\n')
# archivo.close()

# archivo = open('Ejemplo.txt', 'a')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.write('Otro hello world!!!\n')
# archivo.close()

# archivo = open('Data.txt', 'w+')

# for lineas in archivo:
#     print(lineas)

# archivo.write('Hola Mundo\n')

# archivo.close()


lineas = ['Hola Mundo\n', 'Alexanyer\n', 'Alejandra\n']

archivo = open('Data.txt', 'w')

archivo.writelines(lineas)

archivo.close()




