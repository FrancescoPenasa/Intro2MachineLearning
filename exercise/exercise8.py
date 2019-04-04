#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:59:31 2019

@author: francesco

EXERCISE 8
Given the two spirals dataset CSV file, create a 2-dimensional scatter plot of the spirals, 
using a different color for each spiral. 
Then apply the k-nearest neighbors algorithm to all the elements of the dataset 
using k  ∈  {3, 5, 10} and compute precision, accuracy and recall.
    
TIPS:
consider spiral 1 as the positive class
when evaluating, do not include the point you are predicting in the neighbors (this would be cheating)
"""

import pandas as pd
import numpy as np
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
        if distance != 0:
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

def colored_plot(frame, colorMap):
    """
    Plot the frame with different label based on the string colorMap.
    """       
    for pattern in frame[colorMap].unique():
        mask = (frame[colorMap] == pattern)
        points = frame[mask]    
        x = points["x"]
        y = points["y"]
        plt.plot(x, y, 'o', label=pattern)
        
    plt.legend()
    plt.show()


def k_nn_all(df, k, spec):
    """
    k_nn on all the rows of the frame excluding the one tested
    """
    # truePositive, falsePositive, falseNegative, trueNegative
    confusionMatrix = [0,0,0,0] 
    
    for tested in range(df.shape[0]):    
        prediction = k_nn(df, df.iloc[tested], spec, k)    
        if prediction == df.iloc[tested,-1] and prediction == 1:    
            confusionMatrix[0] += 1
        elif prediction != df.iloc[tested,-1] and prediction == 1:    
            confusionMatrix[1] += 1
        elif prediction != df.iloc[tested,-1] and prediction == 0:    
            confusionMatrix[2] += 1
        elif prediction == df.iloc[tested,-1] and prediction == 0:    
            confusionMatrix[3] += 1
    
    accuracy = (confusionMatrix[0]+confusionMatrix[3]) / np.sum(confusionMatrix)
    precision = confusionMatrix[0] / (confusionMatrix[0]+confusionMatrix[1])
    recall = confusionMatrix[0] / (confusionMatrix[0]+confusionMatrix[2])
    
    string = "k: " + str(k) 
    string += "\naccuracy: " + str(accuracy)
    string += ", precision: " + str(precision)
    string += ", recall: " + str(recall)
    print(string)


# --------------------------------------------------------------------------- #
df = pd.read_csv("spirals_density1.csv")
colored_plot(df, "pattern")
k_nn_all(df, 3, "pattern")
k_nn_all(df, 5, "pattern")
k_nn_all(df, 10, "pattern")
