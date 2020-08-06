#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:26:21 2020

@author: mariana
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/home/mariana/Desktop/Soft_Project/spotify_data/data.csv")

#print(df.shape)
print(df.columns)

#print(df.head)


#newdf = df[(df.artists=="Radiohead")]
#newdf = df.query('artists'=="Radiohead")

newdf = df.loc[df['artists'].str.contains('Coldplay', case=False)]
print(newdf)

corr = newdf[['acousticness','danceability','energy',
'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo','valence']].corr()
sns.set(style='darkgrid')

plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True)


most_live = newdf[['name', 'energy', 'liveness']].groupby('name').mean().sort_values(by='energy',ascending=False)[:10]
print(most_live)

most_popular = newdf[['name', 'popularity']].groupby('name').mean().sort_values(by='popularity', ascending=False)
print(most_popular)

most_popular_dependence = newdf[['name', 'popularity', 'acousticness','danceability','energy',
'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo','valence']].groupby('name').mean().sort_values(by='popularity', ascending=False)[:5]
print(most_popular_dependence)