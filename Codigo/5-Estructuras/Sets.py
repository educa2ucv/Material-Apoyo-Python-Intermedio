# conjunto = {1,2,3,4,5,5,5,5,5,5,5,5,5,6,6,6,6}

# conjunto2 = set([1,2,3,4,5,6,7,'Hola','Hola'])

# conjunto.add('Hola Mundo')

# def foo(conjunto):
#     conjunto.remove(5)

# foo(conjunto)

# print(conjunto)

set1 = {1,2,3,4,5,11,122}
set2 = {1,2,3,4,5,6,7,8,9,10,11,12}

# set3 = set1 | set2
# set3 = set1 & set2
set3 = set1 - set2
set4 = set2 - set1

print(set3)
print(set4)

for i in set4:
    print(i)
