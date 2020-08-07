#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:26:21 2020

@author: mariana
"""

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/home/mariana/Desktop/Soft_Project/spotify_data/data.csv")
print(df.columns)



#newdf = df[(df.artists=="Radiohead")]
#newdf = df.query('artists'=="Radiohead")

newdf = df.loc[df['artists'].str.contains(input('Insert your band: '), case=False)]
#print(newdf)

corr = newdf[['acousticness','danceability','energy',
'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo','valence']].corr()
sns.set(style='darkgrid')
plt.figure(figsize=(11,7))
sns.heatmap(corr, annot=True)


most_energetic = newdf[['name', 'energy', 'liveness']].groupby('name').mean().sort_values(by='energy',ascending=False)[:5]
print("The most energetic song")
print(most_energetic)

most_popular = newdf[['name', 'popularity']].groupby('name').mean().sort_values(by='popularity', ascending=False)[:5]
print("The most popular song")
print(most_popular)

most_popular_dependence = newdf[['name', 'popularity', 'acousticness','danceability','energy',
'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo','valence']].groupby('name').mean().sort_values(by='popularity', ascending=False)[:5]
print(most_popular_dependence)