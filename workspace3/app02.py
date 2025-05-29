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
# print('-----------------------------------------')
# print('-----------------------------------------')

# print(tags.iloc[[0,11,2000]])
# print('------------------CABEZA-----------------------')
# print(ratings.head())
# print('-----------------COLA------------------------')
# print(ratings.tail())
# print('-----------------------------------------')
# statistics=ratings['rating'].describe()
# print(statistics)
# print('promedio')
# print(ratings['rating'].mean())
# print('minimo')
# print(ratings['rating'].min())
# print('maximo')
# print(ratings['rating'].max())
# print('media')
# print(ratings['rating'].median())
# print('moda')
# print(ratings['rating'].mode())


# filter=ratings['rating']>5
# print(filter.any())
# print('-----------------------------------------')
# print('-----------------------------------------')

# print('movies')
# print(movies.shape)

# print(movies.isnull().any())

# print('---------------------------------------import pandas as pd

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
# print('-----------------------------------------')
# print('-----------------------------------------')

# print(tags.iloc[[0,11,2000]])
# print('------------------CABEZA-----------------------')
# print(ratings.head())
# print('-----------------COLA------------------------')
# print(ratings.tail())
# print('-----------------------------------------')
# statistics=ratings['rating'].describe()
# print(statistics)
# print('promedio')
# print(ratings['rating'].mean())
# print('minimo')
# print(ratings['rating'].min())
# print('maximo')
# print(ratings['rating'].max())
# print('media')
# print(ratings['rating'].median())
# print('moda')
# print(ratings['rating'].mode())


# filter=ratings['rating']>5
# print(filter.any())
# print('-----------------------------------------')
# print('-----------------------------------------')

# print('movies')
# print(movies.shape)

# print(movies.isnull().any())

# print('-----------------------------------------')
# print('-----------------------------------------')
# print('rating')
# print(ratings.shape)

# print(ratings.isnull().any())

# print('-----------------------------------------')
# print('-----------------------------------------')
# print('tags')
# print(tags.shape)

# print(tags.isnull().any())

# tags=tags.dropna()

# import matplotlib.pyplot as plt

# ratings.hist(figsize=(10, 8), edgecolor='black',color='purple',column='rating')
# plt.suptitle('Histogramas de columnas numéricas')
# plt.show()

# print(ratings.head(10))
# print(ratings.shape)


print('-----------------------------------------')
print('-----------------------------------------')

print(tags.head(3))
tagstwovariableS=tags[['movieId','tag']]
print(tagstwovariableS.head(5))

print(ratings.shape)


samplestaken=ratings[1000:1020]
print(samplestaken.shape)
# print(samplestaken.columns)
print(samplestaken.head(2))

print(tags.head(2))

tags_counts=tags['tag'].value_counts()

print(tags_counts.shape)
print(tags_counts[:10])
# print('-----------------------------------------')
# print('rating')
# print(ratings.shape)

# print(ratings.isnull().any())

# print('-----------------------------------------')
# print('-----------------------------------------')
# print('tags')
# print(tags.shape)

# print(tags.isnull().any())

# tags=tags.dropna()



# ratings.hist(figsize=(10, 8), edgecolor='black',color='purple',column='rating')
# plt.suptitle('Histogramas de columnas numéricas')
# plt.show()

# print(ratings.head(10))
# print(ratings.shape)


print('-----------------------------------------')
import matplotlib.pyplot as plt
print('-----------------------------------------')

print(tags.head(3))
print('-----------------------------------------')
tagstwovariableS=tags[['movieId','tag']]
print(tagstwovariableS.head(5))
print('-----------------------------------------')

print(ratings.shape)


samplestaken=ratings[1000:1020]
print('-----------------------------------------')
print(samplestaken.shape)
print('-----------------------------------------')
print(samplestaken.head(2))
print('-----------------------------------------')
print(tags.head(2))
print('-----------------------------------------')
print(tags.shape)
tags_counts=tags['tag'].value_counts()
print('-----------------------------------------')
print(tags_counts.shape)
print('-----------------------------------------')
print(tags_counts[:10])

tags_counts[:10].plot(kind='bar',figsize=[15,10],color='purple',edgecolor='cyan')
# plt.show()

print(ratings.head(2))
print(ratings.shape)
is_high_rated=ratings['rating']>=4
is_high_rated_df=ratings[is_high_rated]
print(is_high_rated_df.shape)

print('-----------------------------------------')
print('-----------------------------------------')
print(movies.head(3))
print('-----------------------------------------')
print(movies.shape)
print('-----------------------------------------')
# print(movies.columns)
Animation=movies['genres'].str.contains('Animation', case=False, na=False)
Animation_df=movies[Animation]
print(Animation_df.head(5))
print('-----------------------------------------')
print(Animation_df.shape)

print('-----------------------------------------')
print('-----------------------------------------')
ratingcount=ratings[['movieId','rating']].groupby('rating').count()
print(ratings.shape)
print('-----------------------------------------')
print(ratingcount)
print(ratingcount.shape)


avrgrating=ratings[['movieId','rating']].groupby('movieId').mean()
print(avrgrating.shape)
print(avrgrating.head(10))

onerating=ratings[['movieId','rating']].groupby('movieId').count()
print(onerating.shape)
print(onerating.head(10))

