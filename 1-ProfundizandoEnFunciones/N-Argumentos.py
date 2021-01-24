def foo(*args):
    print(args)
    for arg in args:
        print(arg, end='\n')

def foo2(**kwargs):
    print(kwargs['e'])
    # for kwarg in kwargs:
    #     print(f'{kwarg} -> {kwargs[kwarg]}')


# foo2(a=1, b='Hola Mundo', c= True, d= 10*5, e= 'Somos Educa2')

#foo(1,2,3,4,5, 'Hola Mundo', 'Soy Alexanyer', True, False, 2.5)
#print()
foo(1,2,3,4,5, 'Hola Mundo')