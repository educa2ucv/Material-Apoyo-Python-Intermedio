try:
    numero = int(input('Ingrese un numero: '))

    print(f'El numero ingresado más 20 es: { edad + 20 }')
except TypeError:
    print('Hubo un error de tipado')
except NameError:
    print('Hubo un error de nombre')
finally:
    print('Ha finalizado la ejecución del programa')