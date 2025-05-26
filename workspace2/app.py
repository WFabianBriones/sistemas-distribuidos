#!/usr/bin/env python3
import numpy as np
# print('-----------------------------')
# print('numpy')
# print('-----------------------------')
# a=np.array([1,2,3,4,5,6,7,8,9])

# print(a.shape)
# print('elemento extraido del indice 2:',a[2])

# b=np.array([[1,2,3],[11,22,33]])

# print(b.shape)

# print('elemento extraido de la fila 1 y comlumna 2:',b[1,2])


# print(b)
# print('-----------------------------')
# print('ok')
# print('-----------------------------')


# # Clase 02 de Numpy

# print('---------------------------------------------')
# print('Tema')
# print('---------------------------------------------')

# a = np.array([1,2,3,4,5])
# print(a.shape)
# print('El elemento extraído del índice 2 es = ',a[2])

# print('---------------------------------------------')

# b = np.array([[1,2,3],[11,22,33]])
# print(b.shape)
# print(b)
# print('El elemento extraído de la fila 1 y la columna 2 es = ',b[1,2])

# print('---------------------------------------------')

# print('---------------------------------------------')
# print('ZERO / Matrix')
# print('---------------------------------------------')

# # Crear matriz de ceros
# c = np.zeros((5, 4))
# print('Matriz de 0:')
# print(c)

# print('---------------------------------------------')

# # Crear matriz de unos
# d = np.ones((3, 4))
# print('Matriz de 1:')
# print(d)

# print('---------------------------------------------')

# # Crear matriz con el valor 8
# e = np.full((3, 4), 8)
# print('Matriz de valor 8:')
# print(e)

# print('---------------------------------------------')
# print('Práctica')

# # Crear matriz con valores aleatorios entre 1 y 10
# f = np.random.randint(1, 11, (5, 5))
# print('Matriz de valores aleatorios del 1 al 10:')
# print(f)

# print('---------------------------------------------')

# # Crear matriz con números aleatorios entre 0 y 1
# print("Matriz G:")
# g = np.random.random((5, 5))
# print(g)

# print("Matriz identidad:")
# h = np.eye(10)
# print(h)

# # Crear submatriz
# print("SubMatriz:")
# f = np.random.randint(1, 21, (3, 4))  # Genera una matriz de enteros aleatorios entre 1 y 20
# print(f)

# # Extraer submatriz
m = f[:2, :2]
print(m)

# n = np.random.randint(1, 101, size= (7, 5))
# print (n)

# # o = n[:2, :2]
# # print(o)

# h = n[[0, 6, 6, 0], [0, 0, 4, 4]]
# # ([0,7,7,0],[0,0,5,5])
# print(h)
# print(type(h))
# d = h.ndim


# h = n[[0, 2, 3, 5,4,6], [1, 0, 3, 2,0,4]]
# # ([0,7,7,0],[0,0,5,5])
# print(h)
# print(type(h))
# d = h.ndim
# print(d)

# w = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# print(w)
# b=np.array([0,2,0,1])
# c=np.arange(4)
# print(c)
# print('------')
# print(np.arange(4),b)
# w[b,c]+=100
# print(w)


# print('------')
# p = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# print(p)
# filter=(p>5)
# print(filter)
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# z=p[filter]
# print(type(z))
# print(z.shape)
# print(z.ndim)

# print(z)

# print('--------------------------')
# n = np.random.randint(1, 101, size= (15, 15))
# print (n)
# print('--------------------------')
# filter = (n > 40) & (n < 60)
# print(n[filter])
# print('--------------------------')
# print(filter)
# print('--------------------------')
# n[filter]= 0
# print(n)
# print('--------------------------')
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# x=n[filter]
# print(type(x))
# print(x.shape)
# print(x.ndim)


# print('--------------------------')
# m = np.random.randint(1, 101, size= (7, 7))
# print (m)
# print('--------------------------')
# filter = (m % 10==0)
# print(m[filter])
# print('--------------------------')
# print(filter)
# print('--------------------------')
# m[filter]= 200
# print(m)
# print('--------------------------')
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# b=m[filter]
# print(type(b))
# print(b.shape)
# print(b.ndim)



# print('--------------------------')
# m = np.random.randint(1, 101, size= (7, 7))
# print (m)
# print('--------------------------')
# filter = (m % 2 == 1)
# print(m[filter])
# print('--------------------------')
# print(filter)
# print('--------------------------')
# m[filter]= m[filter]**2
# print(m)
# print('--------------------------')
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# b=m[filter]
# print(type(b))
# print(b.shape)
# print(b.ndim)



# print('--------------------------')

a = np.random.randint(1, 10, size= (2, 2))
b = np.random.randint(1, 10, size= (2, 2))
# print('matris a es')
# print(a)
# print('matriz b es')
# print(b)
# print('suma')
# add_m=np.add(a,b)
# print(a+b)
# print('resta')
# print(a-b)
# print('multi')
# print(a*b)
# print('divi')
# print(a/b)
# print('--------------------------')
# aux1=np.subtract(a,b)
# aux2=np.multiply(a,b)
# aux3=np.divide(a,b)
# aux4=np.sqrt(a)

print('--------------------------')


a = np.random.randint(1, 10, size= (3, 3))
b = np.random.randint(1, 10, size= (3, 3))
c=a.dot(b)
print(c)
print(c.shape)
print(c.ndim)


print('--------------------------')

a = np.random.randint(1, 10, size= (4, 6))
b = np.random.randint(1, 10, size= (6, 4))
print('--------------------------')
print(a)
print('--------------------------')
print(b)
print('--------------------------')
c=a.dot(b)
print(c)
print(c.shape)
print(c.ndim)



