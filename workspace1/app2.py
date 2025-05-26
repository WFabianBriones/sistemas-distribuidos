#!/usr/bin/env python3
print('--------------------------------')
print('DICCIONARIO')
print('--------------------------------')
myDictionary={'cat':'cute','dog':'friend','donkey':'hard working'}
print(myDictionary['donkey'])

print('cat' in myDictionary)

myDictionary['fish']='wet'

# for key in myDictionary:
#     feature=myDictionary[key]
#     print('the %s is %s'%(key,feature))

print('--------------------------------')
print('print')
print('--------------------------------')
for key in myDictionary:
    value=myDictionary[key]
    print('the %s is %s'%(key,value))
print('--------------------------------')
print('another way to print')
print('--------------------------------')
for key, value in myDictionary.items():
    print('the %s is %s'%(key,value))
print('--------------------------------')
print('DICIONARIO DEL 1 AL 20')
print('--------------------------------')
myDictN = {x: x**2 for x in range(1, 21)}
print(myDictN)

print('--------------------------------')
print('SET CONTAINER')
print('--------------------------------')
animals={'cat','dog','chicken','monkey','hen'}
print('fish' in animals)
animals.add('fish')
print(animals)
animals.add('mouse')
print(animals)

numberofelements=len(animals)
print(numberofelements)


animals.remove('cat')
print(animals)
print(type(animals))
print(len(animals))


print('--------------------------------')
print('TUPLES')
print('--------------------------------')

tupleDATA=(5,5,5)
print(type(tupleDATA))
print(tupleDATA)

temp_list = list(tupleDATA)
print('agregar 10')
# Agregar un nuevo elemento (por ejemplo, el número 10)
temp_list.append(10)
print(temp_list)
# Eliminar el primer elemento (por ejemplo, el número 5)
print('quitar un 5')
temp_list.remove(5)
print(temp_list)
# Convertir la lista nuevamente a tupla
tupleDATA = tuple(temp_list)
print('resultado')
print(tupleDATA)  # Resultado: (5, 5, 5, 10)


print('--------------------------------')