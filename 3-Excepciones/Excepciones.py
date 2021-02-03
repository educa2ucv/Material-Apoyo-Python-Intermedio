"""
    Las excepciones son bloques de código que nos permiten 
    continuar con la ejecución de un programa pese a que ocurra un error.
"""
bandera = True

while bandera:
    try:
        numero1 = int(input('Ingrese un primer numero: '))
        numero2 = int(input('Ingrese un segundo numero: '))

        print(f'El resultado de la división es: {numero1/numero2}')
    except:
        print('Revise que los valores ingresados sean correctos')
    else:
        bandera = False
        print('No ha sucedido ningún error')
    finally:
        print('Hola desde el finally :)')