#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:37:07 2019

@author: manuel
"""

# Exercise 12
# Implement k-means soft clustering with online update, adopting the Euclidean 
# distance as dissimilarity metric. Given the dataset data3.csv, apply the 
# algorithm using $k = 3$ and $\eta = 0.1$ until the algorithm converges. As 
# initial centroids use $x_{32}, x_{33}, x_{123}$, where the subscripts define 
# the indexes of the points in the dataset. After convergence of the algorithm,
# compute the membership of $x_{10}$ with respect to each centroid and also 
# plot the dataset using different colors for $x_{10}, x_{32}, x_{33}, x_{123}$.

import pandas as pd
import matplotlib.pyplot as plt
import math

def euclidean_distance(s1,s2):
    """
    Compute the Euclidean distance between two n-dimensional objects.
    """    
    tmpsum = 0
    
    for index,value in enumerate(s1):
        tmpsum += (s1[index]-s2[index])**2
    
    return math.sqrt(tmpsum)

def points_difference(point1,point2):
    """
    Compute the difference between two n-dimensional objects and save it in 
    a pandas Series.
    """    
    tmplist = []
    
    for index,value in enumerate(point1):
        tmplist.append(point1[index] - point2[index])
        
    return pd.Series(tmplist)

def points_sum(point1,point2):
    """
    Compute the sum between two n-dimensional objects and save it in 
    a pandas Series.
    """    
    tmplist = []
    
    for index,value in enumerate(point1):
        tmplist.append(point1[index] + point2[index])
        
    return pd.Series(tmplist)

# read data
df = pd.read_csv("data3.csv")  

# set k to be used for k-means clustering
k = 3

# set eta to be used for k-means soft clustering
eta = 0.1

# set training budget
training_budget = 100

# set minimum distance required wrt previous centroids to test convergence
min_distance = 0.01

# initialize variables
centroids = []
previous_centroids = []
iteration = 1

# define indexes to pick initial centroids coordinates
centroids_init_index = [32, 33, 123]

# pick the points from the training set and use them as initial centroids
for i in range(0,k):
    # define initial centroids
    centroids.append(df.iloc[centroids_init_index[i],:])            
    # initialize previous centroids list
    previous_centroids.append(pd.Series([0,0]))

# print data and current centroids   
plt.plot(df["x"],df["y"],'o')
for i in range(0,k):
    plt.plot(centroids[i].iloc[0], centroids[i].iloc[1],'o')
plt.title("Iteration " + str(iteration))
plt.grid(True)
plt.show()    

# -------        

# training loop    
while iteration < training_budget: 
    
    iteration = iteration + 1    

    # iterate over all rows in the dataframe
    for index in range(df.shape[0]):        
        
        # for each data point, compute its soft distance (e^{-distance}) wrt
        # each centroid and the sum of all soft distances
        centroids_soft_distances = []
        sum_soft_distances = 0
        for i in range(0,k):        
            soft_distance = math.exp(-euclidean_distance(centroids[i], df.iloc[index,:]))            
            centroids_soft_distances.append(soft_distance)
            sum_soft_distances = sum_soft_distances + soft_distance                            
        
        # for each data point, compute soft membership and delta wrt each centroid    
        centroids_deltas = []
        for i in range(0,k):
            membership = centroids_soft_distances[i] / sum_soft_distances            
            delta = round(eta * membership * points_difference(df.iloc[index,:], centroids[i]),2)
            centroids_deltas.append(delta)                                                
        
        # update each centroid (online update)
        for i in range(0,k):                            
            centroids[i] = points_sum(centroids[i], centroids_deltas[i])                                 
        
    # print data and current centroids   
    plt.plot(df["x"],df["y"],'o')
    for i in range(0,k):
        plt.plot(centroids[i].iloc[0], centroids[i].iloc[1],'o')
    plt.title("Iteration " + str(iteration))        
    plt.grid(True)
    plt.show()                  
    
    # check for convergence after having iterated over all points, because
    # the update is done online
    
    # loop until the positions of the centroids do not change anymore (2 dimensions)
    sum_distances = 0
    for i in range(0,k):
        sum_distances = sum_distances + euclidean_distance(previous_centroids[i],centroids[i])    
    if(sum_distances <= min_distance):
        break              
    
    # before getting updated, current centroids are saved
    previous_centroids = list(centroids)        

# -------

# compute membership for a particular point
point_index = 10
    
# print data, centroids and the given point
plt.plot(df["x"],df["y"],'o')
for i in range(0,k):
    plt.plot(centroids[i].iloc[0], centroids[i].iloc[1],'o')
plt.plot(df.iloc[point_index,0], df.iloc[point_index,1],'o', color="red")
plt.title("Position of centroids (and $x_{10}$) after convergence")
plt.grid(True)
plt.show()

# compute soft distances of x_10 wrt centroids
centroids_soft_distances = []
sum_soft_distances = 0
for i in range(0,k):        
    soft_distance = math.exp(-euclidean_distance(centroids[i], df.iloc[point_index,:]))
    centroids_soft_distances.append(soft_distance)
    sum_soft_distances = sum_soft_distances + soft_distance

# membership of x_10 wrt centroids
print("Membership of x_10 wrt centroids after convergence:")    
for i in range(0,k):
    membership = centroids_soft_distances[i] / sum_soft_distances
    print(membership)

# -------    