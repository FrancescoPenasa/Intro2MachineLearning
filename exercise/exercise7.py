#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:10:18 2019
@author: francesco

Given the iris dataset CSV file and a new unseen vector representing a flower, 
define a function that classifies the new flower using its k-nearest neighbors. 
Apply the algorithm using k in {5,10,20} and print the label of the results.

Also, create 2-dimensional scatter plots of the iris dataset considering the given pairs of dimensions, 
and draw the points of each class with a different color. 
Take a look at the plots and answer the following question: 
    if you could use only one of the given pairs to apply k-nearest neighbors, 
    which pair would you use?

TIPS:
* the plots should be similar to the following:
"""

import pandas as pd
import numpy as np
import sys 

newFlower = [5.8, 3.0, 4.9, 1.6]
pairs = [("SepalLength","SepalWidth"),
         ("PetalLength","PetalWidth"),
         ("PetalLength","SepalLength"),
         ("PetalWidth","SepalWidth")]


def k_nearest_neighbors (db, new_flower, k):
    #init dictionary
    neighbors = []
    flowers = []
    for i in range(k):
        neighbors.append(sys.maxsize)
        flowers.append(-1)

    # for all elements in db 
    for n in range(len(db)):
        old_flower = df.iloc[n,0:4]                     #take one elem
        res = np.linalg.norm(old_flower - new_flower)   #compare it 
        
        light = True
        for index in range(k):
            if res <= neighbors[index-1] and light:
                light = False
                neighbors[-1] = res
                neighbors = sorted(neighbors)
                flowers.insert(index,n)
    
    print(neighbors)
    print(flowers[0:k])
    
    names = {}
    for n in range(k):
        print(db.iloc[flowers[n], 4])
        if db.iloc[flowers[n], 4] in names.keys():
            names[db.iloc[flowers[n], 4]] += 1
        else:
            names[db.iloc[flowers[n], 4]] = 0
     
    v=list(names.values())
    k=list(names.keys())
    print("\n And the winner is: ",k[v.index(max(v))])

df = pd.read_csv("iris.data", names = ["param0","param1", "param2", "param3", "name"])
k_nearest_neighbors(df, newFlower, 5)
print("")
k_nearest_neighbors(df, newFlower, 10)
print("")
k_nearest_neighbors(df, newFlower, 15)
