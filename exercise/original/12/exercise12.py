#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:37:07 2019

@author: manuel
"""

# Exercise 12
# Given some 2-dimensional dataset like data1.csv, data2.csv or data3.csv, 
# implement and apply k-means hard clustering with k = 2 and k = 3. 
# Use the Euclidean distance as dissimilarity metric.
# At each training iteration of the algorithm, compute the quantization error
# and plot data points and centroids with a different color for each cluster.

import numpy as np
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

# read data 
df = pd.read_csv("data3.csv")  

# plot data
plt.plot(df["x"], df["y"], 'o')
plt.title("Data")
plt.grid(True)
plt.show()

# set k to be used for k-means clustering
k = 3
training_budget = 100

# init variables
centroids = []          # centroids coordinates
previous_centroids = [] # centroids of previous training iteration
iteration = 1           # training iteration

# get random indexes between 1 and # of data points to pick initial centroids
np.random.seed(2)
centroids_init_index = np.random.randint(1, len(df), k)

for i in range(0,k):
    # define initial centroids from training data using the random indexes
    centroids.append(df.iloc[centroids_init_index[i],:])                
    # initialize variables to consider centroids of the previous training iteration
    previous_centroids.append(pd.Series([0,0]))
    
# training loop    
while iteration < training_budget: 

    # loop until the positions of the centroids do not change anymore (2 dimensions)
    sum_distances = 0
    for i in range(0,k):
        sum_distances = sum_distances + euclidean_distance(previous_centroids[i],centroids[i])        
    if(sum_distances == 0):
        break
        
    # init varibles
    centroids_lists = []            # list of dataframes of points assigned to each centroid
    centroids_lists_distances = []  # list of dataframes of distances wrt to each centroid
    
    for i in range(0,k):
        # define an empty dataframe for the points assigned to each centroid
        centroids_lists.append(pd.DataFrame())        
        # define an empty dataframe for the distances between each point
        # of a cluster and the respective centroid
        centroids_lists_distances.append(pd.DataFrame())        
    
    # iterate over all rows in the dataframe (data point), to find nearest centroid
    for index in range(df.shape[0]):
        
        # get all columns of a row
        point = df.iloc[index,:]        
    
        # init variables
        minimum_distance = 100      # min distance found between current point and nearest centroid
        nearest_centroid_index = -1 # index of the nearest centroid wrt current point
    
        # given a data point, compute the distance wrt each centroid and find the nearest centroid
        for centroid_index,centroid in enumerate(centroids):
            distance = euclidean_distance(point, centroid)
            if(distance < minimum_distance):
                minimum_distance = distance
                nearest_centroid_index = centroid_index                  
                
        # append data point according to the index of its nearest centroid
        centroids_lists[nearest_centroid_index] = centroids_lists[nearest_centroid_index].append(point)
        
        # append minimum distance according to the index of nearest centroid of current point
        # (to compute quantization error)
        centroids_lists_distances[nearest_centroid_index] = centroids_lists_distances[nearest_centroid_index].append(pd.Series([minimum_distance]), ignore_index=True)

    # compute quantization error
    tmp_sum = 0
    for i in range(0,k):                 
        # square all minimum distances wrt the centroid for one cluster
        tmp = centroids_lists_distances[i].iloc[:,0]**2
        tmp_sum = tmp_sum + tmp.sum()    
    qe = tmp_sum / k

    # print current clusters and centroids
    for i in range(0,k):        
        # print cluster
        plt.plot(centroids_lists[i].iloc[:,0], centroids_lists[i].iloc[:,1], 'o')        
        # print centroid
        plt.plot(centroids[i].iloc[0], centroids[i].iloc[1],'o')        
    plt.title("Iteration " + str(iteration) + ": QE = " + "{0:.2f}".format(qe))
    plt.grid(True)
    plt.show()
    
    # compute new centroid coordinates as mean of the points in each cluster
    previous_centroids = centroids
    centroids = []
    for i in range(0,k):        
        centroids.append(centroids_lists[i].mean())    
        
    iteration = iteration + 1