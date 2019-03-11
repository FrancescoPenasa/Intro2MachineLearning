#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:10:18 2019
@author: francesco
"""
#Given the iris dataset CSV file and a new unseen vector representing a flower, 
#define a function that classifies the new flower using its k-nearest neighbors. 
#Apply the algorithm using k in {5,10,20} and print the label of the results.
#
#Also, create 2-dimensional scatter plots of the iris dataset considering the given pairs of dimensions, 
#and draw the points of each class with a different color. 
#Take a look at the plots and answer the following question: 
#    if you could use only one of the given pairs to apply k-nearest neighbors, 
#    which pair would you use?
#
#TIPS:
#* the plots should be similar to the following:
 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 

newFlower = [5.4, 3.8, 1.7, 0.3]
pairs = [("SepalLength","SepalWidth"),
         ("PetalLength","PetalWidth"),
         ("PetalLength","SepalLength"),
         ("PetalWidth","SepalWidth")]



def near_flower(db, new_flower):
    nearest_distance = sys.maxsize
    nearest_flower_index = -1
    for flower in range(db.shape[0]):
        stored_flower = db.iloc[flower,0:4]    
        distance = np.linalg.norm(stored_flower - new_flower)
        if nearest_distance >= distance:
            nearest_distance = distance
            nearest_flower_index = flower;
    print(nearest_flower_index)
    return nearest_flower_index;


def k_nearest_neighbors(df, newFlower, k):
    mask = (df["names"] != None)
    db = df[mask]
    
    bestFlowers = []
    nameFlowers = pd.unique(df.iloc[:,-1])
    
    nearFlower = near_flower(db, newFlower)
    bestFlowers.append(nearFlower)
        
    mask[nearFlower] = False 
    db = df[mask]    
        
    
    print(mask)
    
    print(db)
    
   
    
    nearFlower = near_flower(db, newFlower)
    bestFlowers.append(nearFlower)    
    mask[nearFlower] = False 
    db = df[mask]    
        
    
    print(mask)
    
    print(db)
    
    
#    
#    for i in len(bestFlowers):
#        print (db[bestFlowers[i],-1])
    
        
df = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth", "PetalLength", "PetalWidth", "names"])

k_nearest_neighbors(df, newFlower, 20)
        
        
        
    
#
#def k_nearest_neighbors (db, new_flower, k):
#    #init dictionary
#    neighbors = []
#    flowers = []
#    for i in range(k):
#        neighbors.append(sys.maxsize)
#        flowers.append(-1)
#
#    # for all elements in db 
#    for n in range(len(db)):
#        old_flower = df.iloc[n,0:4]                     #take one elem
#        res = np.linalg.norm(old_flower - new_flower)   #compare it 
#        
#        light = True
#        for index in range(k):
#            if res <= neighbors[index-1] and light:
#                light = False
#                neighbors[-1] = res
#                neighbors = sorted(neighbors)
#                flowers.insert(index,n)
#    names = {}
#    for n in range(k):
#        if db.iloc[flowers[n], 4] in names.keys():
#            names[db.iloc[flowers[n], 4]] += 1
#        else:
#            names[db.iloc[flowers[n], 4]] = 0
#     
#    v=list(names.values())
#    k=list(names.keys())
#    print("\n And the winner is: ",k[v.index(max(v))])

#print("")
#k_nearest_neighbors(df, newFlower, 10)
#print("")
#k_nearest_neighbors(df, newFlower, 20)


#listnames = []
#parameters = enumerate(["SepalLength","SepalWidth", "PetalLength", "PetalWidth", "names"])
#for flower in df.index:
#    if df.iloc[flower, -1] in listnames:
#        plt.plot(df.iloc[flower, 0], df.iloc[flower, 1], 'o', label=listnames, c=colors)
#    else:
#        listnames.append(df.iloc[flower, -1])
#        colors = np.random.rand(3,)
#        plt.plot(df.iloc[flower, 0], df.iloc[flower, 1], 'o', label=listnames, c=colors)
#plt.show()    
#    
#
#listnames = []
#for flower in df.index:
#    if df.iloc[flower, -1] in listnames:
#        plt.plot(df.iloc[flower, 0], df.iloc[flower, 2], 'o', label=listnames, c=colors)
#    else:
#        listnames.append(df.iloc[flower, -1])
#        colors = np.random.rand(3,)
#        plt.plot(df.iloc[flower, 0], df.iloc[flower, 2], 'o', label=listnames, c=colors)
#plt.show()  
#
#listnames = []
#for flower in df.index:
#    if df.iloc[flower, -1] in listnames:
#        plt.plot(df.iloc[flower, 1], df.iloc[flower, 3], 'o', label=listnames, c=colors)
#    else:
#        listnames.append(df.iloc[flower, -1])
#        colors = np.random.rand(3,)
#        plt.plot(df.iloc[flower, 1], df.iloc[flower, 3], 'o', label=listnames, c=colors)
#plt.show()  
#
#listnames = []
#for flower in df.index:
#    if df.iloc[flower, -1] in listnames:
#        plt.plot(df.iloc[flower, 2], df.iloc[flower, 3], 'o', label=listnames, c=colors)
#    else:
#        listnames.append(df.iloc[flower, -1])
#        colors = np.random.rand(3,)
#        plt.plot(df.iloc[flower, 2], df.iloc[flower, 3], 'o', label=listnames, c=colors)
#plt.legend(listnames)
#plt.show()  
