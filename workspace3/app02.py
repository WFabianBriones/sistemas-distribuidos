import pandas as pd

print('case studies: movies anda data analysis')
print('-----------------------------------------')
print('MOVIES')
movies=pd.read_csv('movies.csv')
print(movies.head(2))
print(movies.columns)
print(movies.index)
print(movies.shape)
print('-----------------------------------------')
print('TAGS')
tags=pd.read_csv('tags.csv')
print(tags.head(2))
print(tags.columns)
print(tags.index)
print(tags.shape)
print('-----------------------------------------')
print('RATING')
ratings=pd.read_csv('ratings.csv')
print(ratings.head(2))
print(ratings.columns)
print(ratings.index)
print(ratings.shape)
print('ok')
print('-----------------------------------------')
print('-----------------------------------------')
print('ELIMIMAR TIMESTAMP')
print('-----------------------------------------')
del ratings['timestamp']
print('-----------------------------------------')
del tags['timestamp']
print(tags.head(2))
print(ratings.head(2))
print('-----------------------------------------')
print('-----------------------------------------')

print(tags.iloc[[0,11,2000]])
print('------------------CABEZA-----------------------')
print(ratings.head())
print('-----------------COLA------------------------')
print(ratings.tail())
print('-----------------------------------------')
statistics=ratings['rating'].describe()
print(statistics)
print('promedio')
print(ratings['rating'].mean())
print('minimo')
print(ratings['rating'].min())
print('maximo')
print(ratings['rating'].max())
print('media')
print(ratings['rating'].median())
print('moda')
print(ratings['rating'].mode())


filter=ratings['rating']>5
print(filter.any())
print('-----------------------------------------')
print('-----------------------------------------')

print('movies')
print(movies.shape)

print(movies.isnull().any())

print('-----------------------------------------')
print('-----------------------------------------')
print('rating')
print(ratings.shape)

print(ratings.isnull().any())

print('-----------------------------------------')
print('-----------------------------------------')
print('tags')
print(tags.shape)

print(tags.isnull().any())

tags=tags.dropna()

import matplotlib.pyplot as plt

ratings.hist(figsize=(10, 8), edgecolor='black',color='purple',column='rating')
plt.suptitle('Histogramas de columnas numéricas')
plt.show()

print(ratings.head(10))
print(ratings.shape)

