#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:35:51 2019

@author: manuel
"""

# Exercise 8
# Given the two spirals CSV file, create a 2-dimensional scatter plot of the 
# spirals using a different color for each spiral. Then apply the k-nearest
# neighbors algorithm to all the elements of the dataset using k = {3, 5, 10} 
# and compute precision, accuracy and recall.

import math
import pandas as pd
import matplotlib.pyplot as plt

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
        # when evaluating, do not include the point to be predicted in the solution
        # (this would be cheating)
        if(distance!=0):
            distances.append((distance, frame.iloc[index,-1]))                

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

def plot_data(frame, col1, col2, colClass):
    """
    Print a 2-d scatter plot of the points in the dataframe using col1 and col2;
    the string colClass is the label, used to decide the color of the points.
    """
    # for each class, print the data points
    for label in frame[colClass].unique():    
        mask = (frame[colClass] == label)
        points = frame[mask]	    
        plt.plot(points[col1], points[col2], 'o', label=label)
        
    plt.title(col1+" vs "+ col2)
    plt.legend()
    plt.grid(True)
    plt.show()
    
def compute_classification_metrics(frame, colClass, k):
    """
    Compute accuracy, precision and recall after having classified all points 
    of the dataset using k-nearest neighbors.
    """
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    
    # iterate over all rows of the dataframe
    for i in range(frame.shape[0]):
        
        # extract the row from the dataframe
        flower = frame.iloc[i,:]
            
        # predict the label using k-nn
        prediction = k_nn(frame, flower.tolist()[:-1], colClass, k)
        
        # count true positives, false positives, false negatives, true negatives
        # (considering elements of spiral 1 as positives)
        if(flower[-1] == 1)and(flower[-1] == prediction):
            tp += 1
        elif(flower[-1] == 0)and(flower[-1] != prediction):
            fp += 1        
        elif(flower[-1] == 1)and(flower[-1] != prediction):
            fn += 1        
        elif(flower[-1] == 0)and(flower[-1] == prediction):
            tn += 1                    
            
    # compute the metrics using the formulas            
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    
    return (accuracy, precision, recall)

# -----------------------------------------------------------------------------

# read data
frame = pd.read_csv("/home/manuel/Dropbox/PhD/teaching/intro-to-ML/lecture4/material/spirals_density1.csv")

# plot the spirals
plot_data(frame,"x","y","pattern")

# compute and print classification metrics
k = 3
metrics = compute_classification_metrics(frame, "pattern", k)
tmpString = "{0:.2f}"
print("Using k =", k, ": Accuracy =", tmpString.format(metrics[0]), 
      "precision =", tmpString.format(metrics[1]),
      "recall =", tmpString.format(metrics[2]))

k = 5
metrics = compute_classification_metrics(frame, "pattern", k)
tmpString = "{0:.2f}"
print("Using k =", k, ": Accuracy =", tmpString.format(metrics[0]), 
      "precision =", tmpString.format(metrics[1]),
      "recall =", tmpString.format(metrics[2]))

k = 10
metrics = compute_classification_metrics(frame, "pattern", k)
tmpString = "{0:.2f}"
print("Using k =", k, ": Accuracy =", tmpString.format(metrics[0]), 
      "precision =", tmpString.format(metrics[1]),
      "recall =", tmpString.format(metrics[2]))