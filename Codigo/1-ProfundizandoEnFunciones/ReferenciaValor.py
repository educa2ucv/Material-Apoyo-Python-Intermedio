variable_uno = 100
variable_dos = [ x for x in range(1,11) ]

def foo(n):
    n += 100*500
    return n 

def foo2(lista):
    lista.append(11)
    lista.append(12)
    lista.append(13)
    lista.append(14)
    lista.append(15)

print(variable_dos)
foo2(variable_dos)
print(variable_dos)

#resultado = foo(variable_uno)
#print(variable_uno,resultado)   