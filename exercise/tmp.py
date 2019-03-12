#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
import math

def euclidean_distance(s1,s2):
    """
    Compute the Euclidean distance between two n-dimensional objects.
    """    
    tmpsum = 0
    
    for index,value in enumerate(s1):
        tmpsum += (s1[index]-s2[index])**2
    
    return math.sqrt(tmpsum)

def near_flower(db, new_flower):
    nearest_distance = sys.maxsize
    nearest_flower_index = -1
    for flower in range(db.shape[0]):
        stored_flower = db.iloc[flower,0:4]    
        distance = euclidean_distance(stored_flower, new_flower)
        if nearest_distance >= distance:
            nearest_distance = distance
            nearest_flower_index = flower;
    return nearest_flower_index;


def k_nearest_neighbors(df, newFlower, k):
    mask = [True for n in range(df.shape[0])]
    db = df[mask]
    
    bestFlowers = []
    nameFlowers = pd.unique(df.iloc[:,-1])
    
    while k > 0:
        nearFlower = near_flower(db, newFlower)
        bestFlowers.append(nearFlower)
        mask[nearFlower] = False 
        db = df[mask]    
        k -= 1
    print(bestFlowers)
    occurencies = {}    
    for name in nameFlowers:
        occurencies[name] = 0
    for flower in bestFlowers:
        name = df.iloc[flower, -1]
        occurencies[name] += 1
    
    print(occurencies)
        
df = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth", "PetalLength", "PetalWidth", "names"])
newFlower = [5.8, 3.0, 4.9, 1.6]

k_nearest_neighbors(df, newFlower, 5)