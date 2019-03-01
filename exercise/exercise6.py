#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:10:18 2019
@author: francesco

Given the iris dataset CSV file and a new unseen vector representing a flower, 
define a function that classifies the new flower according to the class of its nearest neighbor.
TIPS: 
    * use the Euclidean distance as distance metric
    * you can download and find more information about the iris dataset at 
    https://archive.ics.uci.edu/ml/datasets/iris.
"""

import pandas as pd
import numpy as np


new_flower = np.array([5.2,2.3,3.2,1.1])

df = pd.read_csv("iris.data", names = ["param0","param1", "param2", "param3", "name"])

def near_flower(df, new_flower):
    lowest_distance = np.inf
    lowest_flower_index = -1
    for n in range(len(df)):
        old_flower = df.iloc[n,0:4]    
        res = np.linalg.norm(old_flower - new_flower)
        if lowest_distance >= res:
            lowest_distance = res
            lowest_flower_index = n;
    print("new flower: ", new_flower,)
    print(lowest_flower_index)
    print("is a: ", df.iloc[lowest_flower_index][4])
    print(df.iloc[lowest_flower_index])

near_flower(df, new_flower)