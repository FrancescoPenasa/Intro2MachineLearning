#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:59:31 2019

@author: francesco
"""

#Given the two spirals dataset CSV file, create a 2-dimensional scatter plot of the spirals, 
#using a different color for each spiral. 
#Then apply the k-nearest neighbors algorithm to all the elements of the dataset 
#using k  ∈  {3, 5, 10} and compute precision, accuracy and recall.
#
#TIPS:
#
#consider spiral 1 as the positive class
#when evaluating, do not include the point you are predicting in the neighbors (this would be cheating)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("spirals_density1.csv")
print(df)


for pattern in df["pattern"].unique():
    mask = (df["pattern"] == pattern)
    points = df[mask]    
    x = points["x"]
    y = points["y"]
    plt.plot(x, y, 'o', label=pattern)
    
plt.legend()
plt.show()