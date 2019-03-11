#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:06:39 2019

@author: francesco
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 

newFlower = [5.8, 3.0, 4.9, 1.6]


def k_nearest_neighbors(df, newFlower, k):
    mask = (df["names"] != None)
    db = df[mask]
    
    mask[19] = False
    print(db)    
    db = df[mask]
    print(db["PetalLength"]) 
#    for i in len(bestFlowers):
#        print (db[bestFlowers[i],-1])
    
        
df = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth", "PetalLength", "PetalWidth", "names"])

k_nearest_neighbors(df, newFlower, 20)
        