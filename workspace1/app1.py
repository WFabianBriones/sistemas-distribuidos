
#!/usr/bin/env python3
# hello world
print('FabianUwu')

variable1=12
variable2=12.0
variable3=True
variable4='Washingtom Briones'

print(variable1)
print(variable2)
print(variable3)
print(variable4)

# list

list1=[1,2,3,4,5,6,'fabian',True]
print(list1[1])
print(list1[3])

#dictionary
dict1={'student1':'josue','student2':'mateo'}
print(dict1['student2'])

stringvariable='3'
print(type(stringvariable))
numericalvariable=int(stringvariable)
print(type(numericalvariable))


print('----------------------------------------')
print('control flow')

age=30

message1='you are yunger'
message2='you are old'


if age>=25:
    print(message2)
else:
    print(message1)

if age>30:
    print(message2)
elif age<30:
    print(message1)
elif age==30:
    print('you have the right age, congratulation')

print('----------------------------------------')
print('loop for')
for i in list1:
    print('element inside the list', i)

print('----------------------------------------')
print('dict')
for i in dict1.values():
    print('element inside the dic', i)


print('----------------------------------------')
print('funciones')

def message():
    print('hello fon the funcion message')

message()

for i in range(10):
    message()

# print('----------------------------------------')
# print('mostrar nombre y edad')

# name=input('enter your name: ')
# age=int(input('enter your age: '))


# def message1(age,name):
#     print('your are young')
#     print(f'your name is {name} and your age is {age}')

# def message2(age,name):
#     print('your are old')
#     print(f'your name is {name} and your age is {age}')


# def message3(age,name):
#     print('you have the right age, congratulation')
#     print(f'your name is {name} and your age is {age}')

# if age<30:
#     message1(age,name)
# elif age>50:
#     message2(age,name)
# else:
#     message3(age,name)


# while True:
#     print('----------------------------------------')
#     print('mostrar nombre y edad')

#     name = input('enter your name: ')
#     age = int(input('enter your age: '))

#     def message1(age, name):
#         print('you are young')
#         print(f'your name is {name} and your age is {age}')

#     def message2(age, name):
#         print('you are old')
#         print(f'your name is {name} and your age is {age}')

#     def message3(age, name):
#         print('you have the right age, congratulations')
#         print(f'your name is {name} and your age is {age}')

#     if age < 30:
#         message1(age, name)
#     elif age > 50:
#         message2(age, name)
#     else:
#         message3(age, name)

#     # Ask if the user wants to continue
#     continue_prompt = input("Do you want to enter another name and age? (yes/no): ")
#     if continue_prompt.lower() != 'yes':
#         break


print('----------------------------------------')
print('potencia')
list3=[1,2,3,4,5]
listasquare=[]

for item in list3:
    listasquare.append(item**2)
for item in listasquare:
    print(item)


print('----------------------------------------')
print('raiz')

import math
listasquare=[]

for item in list3:
    listasquare.append(math.sqrt(item))

print('raiz cuadrada de mi lista')

for i in listasquare:
    print(i)
