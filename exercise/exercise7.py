#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:10:18 2019
@author: francesco

Exercise 7
 Given the iris dataset CSV file and a new unseen vector representing a flower, 
 define a function that classifies the new flower using its k-nearest neighbors. 
 Apply the algorithm using k = {5, 10, 20} and print the label of the results.

 Also, create 2-dimensional scatter plots of the iris dataset considering the 
 given pairs of dimensions, and draw the points of each class with a different 
 color.

 Take a look at the plots and answer the following question: if you could use 
 only one of the given pairs to apply k-nearest neighbors, which pair would 
 you use?
"""

import pandas as pd
import math
import matplotlib.pyplot as plt
import sys

def euclidean_distance(s1,s2):
    """
    Compute the Euclidean distance between two n-dimensional objects.
    """    
    tmpsum = 0
    
    for index,value in enumerate(s1):
        tmpsum += (s1[index]-s2[index])**2
    
    return math.sqrt(tmpsum)

def find_distances(frame, newPoint):
    """
    Find the distance between a point and all the points in a dataframe, and
    sort the elements in ascending order.
    """                
    distances = []    
    
    # iterate over all rows in the dataframe
    for index in range(frame.shape[0]):

        # get all columns of a row (except the label) 
        point = frame.iloc[index,:-1]        

    	# compute the distance, then save distance and label 
        # (use distance as first value)
        distance = euclidean_distance(point, newPoint)
        if distance == 0:
            distances.append((distance, frame.iloc[index,-1]))                
        else:
            distances.append((sys.maxsize, frame.iloc[index,-1]))                
            

    distances.sort()    
    
    return distances

def k_nn(frame, newPoint, colClass, k):
    """
    Predict the class of a point by using the k-nearest neighbor algorithm on 
    the points of a dataframe.
    """                
    counts = []
    
    # find all distances wrt the newPoint
    dist = find_distances(frame, newPoint)

    # find the nearest k points, extract their labels and save them in a list
    labels = [label for distance,label in dist[:k]] 
    
    # for each class label, count how many occurrencies have been found
    for label in frame[colClass].unique():
        # save the number of occurrencies in a list of tuples (number, label)
        counts.append((labels.count(label), label))        
    
    # sort the list in descending order, and use the first label of the tuples'
    # list to make the prediction    
    counts.sort(reverse=True)
    prediction = counts[0][1]    
    
    return prediction


def colored_plot_pairs(frame, pairs, colorMap):
    """
    Plot the frame with different label based on the string colorMap.
    """       
    for i in range(len(pairs)):
        x_label = pairs[i][0]
        y_label = pairs[i][1]
        
        for pattern in frame[colorMap].unique():
            mask = (frame[colorMap] == pattern)
            points = frame[mask]    
            x = points[x_label]
            y = points[y_label]
            plt.title(x_label+"-"+y_label)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.plot(x, y, 'o', label=pattern)
            
        plt.grid(True)
        plt.legend()
        plt.show()

# -----------------------------------------------------------------------------

# read and define data
frame = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth","PetalLength","PetalWidth","Class"])
newFlower = [5.8, 3.0, 4.9, 1.6]

# compute the prediction using different k
k = 5
prediction = k_nn(frame, newFlower, "Class", k)
print("Using k-nearest neighbors with k =", str(k) + ",the point", newFlower, 
      "is classified as", prediction)

k = 10
prediction = k_nn(frame, newFlower, "Class", k)
print("Using k-nearest neighbors with k =", str(k) + ",the point", newFlower, 
      "is classified as", prediction)

k = 20
prediction = k_nn(frame, newFlower, "Class", k)
print("Using k-nearest neighbors with k =", str(k) + ",the point", newFlower, 
      "is classified as", prediction)

# plot data using the given pairs
pairs = [("SepalLength","SepalWidth"),
         ("PetalLength","PetalWidth"),
         ("PetalLength","SepalLength"),
         ("PetalWidth","SepalWidth")]

colored_plot_pairs(frame, pairs, "Class")
