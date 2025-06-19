#!/usr/bin/env python3

import pandas as pd


print('---------------------------------------------------')
print('loading dataset')
print('---------------------------------------------------')
tangs=pd.read_csv('tags.csv')

ratings=pd.read_csv('ratings.csv')

movies=pd.read_csv('movies.csv')


print('---------------------------------------------------')
print('tags')
print(tangs.columns)
print('---------------------------------------------------')
print('ratings')
print(ratings.columns)  
print('---------------------------------------------------')
print('movies')
print(movies.columns)
print('---------------------------------------------------')
print('marge data frame')
print('---------------------------------------------------')
df=movies.merge(tangs, on='movieId',how='inner')
print(df.columns)
print('---------------------------------------------------')
print(df.head(3))
print('---------------------------------------------------')
avg_ratings=ratings.groupby('movieId',as_index=False).mean()
print(avg_ratings.head(3))
print('---------------------------------------------------')
del avg_ratings['userId']
print(avg_ratings.head(3))

print('---------------------------------------------------')
print('---------------------------------------------------')
df2=movies.merge(avg_ratings, on='movieId',how='inner')
filter=df2['rating']>=4.0
print('---------------------------------------------------')
print(df2[filter][-5:])
print(df2.columns)


print('---------------------------------------------------')
print('---------------------------------------------------')
print(tangs.columns)
print(tangs['timestamp'].dtype)

tangs['etrfm']=pd.to_datetime(tangs['timestamp'],unit='s')
print(tangs.columns)
print(tangs['etrfm'].dtype)
print(tangs['etrfm'][-5:])

greater_than_t=tangs['etrfm']>'2015-02-01'
df3=tangs[greater_than_t]


print('df3')
print(df3.shape)
print('tags')   
print(tangs.shape)