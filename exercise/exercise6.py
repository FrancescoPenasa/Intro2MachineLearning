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
import sys


new_flower = np.array([5.2,2.3,3.2,1.1])

df = pd.read_csv("iris.data", names = ["param0","param1", "param2", "param3", "name"])

def near_flower(db, new_flower):
    nearest_distance = sys.maxsize
    nearest_flower_index = -1
    for flower in range(len(df)):
        stored_flower = db.iloc[flower,0:4]    
        distance = np.linalg.norm(stored_flower - new_flower)
        if nearest_distance >= distance:
            nearest_distance = distance
            nearest_flower_index = flower;
    print(nearest_flower_index)
    return nearest_flower_index;

near_flower(df, new_flower)