#test = 'Hola Mundo desde la funcion global'
test2 = 100

def foo():
    global test2
    #test = 'Hola Mundo desde foo'
    test2 += 200
    # test2 = test2 + 200
    
foo()
print(test2)