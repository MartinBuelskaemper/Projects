# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:01:39 2018

@author: Marti
"""
from sklearn import tree #decison tree


# [height, weight, shoe size]
X = [[181,80,44],[177,70,43],[160,60,38],[181,85,43],[166,65,40],[177,70,40]]

Y = ['male','male','female','male','female','male']

clf = tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction)