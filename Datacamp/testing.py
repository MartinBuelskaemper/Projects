# -*- coding: utf-8 -*-
"""
Created on 2018-11-17 18:49

Creator: Martin Buelskaemper
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', sep=';')

print(df.loc[:,['device','price']])

nums = [2, 4, 6, 8, 10]

x = [5, 4, 4, 5, 5]
y = [2, 4, 8, 9, 10]
z = [3, 4, 7, 8, 11]

result = list(map(lambda a: a ** 2, nums)) #Wichtig

hallo = list(filter(lambda a: a>5, nums)) #Wichtig

#print(np.corrcoef([x,y,z])) #Wichtig

#plt.scatter(x,y)
#plt.show()

planets = {
    'planet': ['earth', 'mars', 'jupiter'],
    'length_of_day': ['1', '1.03', '0.414']
}

df_planets = pd.DataFrame(planets)

for i,j in df_planets.iterrows():
    print(str(i)+' '+str(j['planet']))

print(df_planets)
