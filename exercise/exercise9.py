#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:50:04 2019

@author: francesco

Given the iris dataset CSV file, 
apply the k-nearest neighbors algorithm to all the elements of the dataset 
using k  ∈  {3, 5, 10, 20} and build the confusion matrix. 
Using the confusion matrix, compute total precision, total accuracy and total recall.

TIPS:

total metrics correspond to the average of the relative metric computed on the elements of each class
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

def compute_accuracy(confusionMatrix): 
    """
    Compute accuracy based on a Confusion Matrix 
    with prediction on rows 
    and truth on columns.
    """  
    correct = 0
    for elem in range(confusionMatrix.shape[0]):
        correct += confusionMatrix[elem, elem] 
    tot = confusionMatrix.sum()
    return correct / tot
    
def compute_precision(confusionMatrix): 
    """
    Compute precision based on a Confusion Matrix 
    with prediction on rows 
    and truth on columns.
    precision = true positive / (true positive + false positive)
    """    
    precision = []
    for i in range(confusionMatrix.shape[0]):
        tot = 0
        for j in range(confusionMatrix.shape[0]):
            tot += confusionMatrix[i, j]  
        correct = confusionMatrix[i, i] 
        precision.append(correct/tot)
    return precision
        
def compute_recall(confusionMatrix):
    """
    Compute recall based on a Confusion Matrix 
    with prediction on rows 
    and truth on columns.
    recall = true positive / (true positive + false negative)
    """  
    recall = []
    for elem in range(confusionMatrix.shape[0]):
        tot = 0
        for j in range(confusionMatrix.shape[0]):
            tot += confusionMatrix[j, elem]  
        correct = confusionMatrix[elem, elem] 
        recall.append(correct/tot)
    return recall

def init_confusionMatrix(df, spec):
    """
    Init confusion matrix with rows and columns based on the df[spec].unique()
    """
    rows = 0
    names = []
    for name in df[spec].unique():
        rows += 1
        names.append(name)
    confusionMatrix = [[0] * rows for x in range(rows)]
    confusionMatrix = np.matrix(confusionMatrix)
    return confusionMatrix,names

def k_nn_all(df, k, spec):
    """
    k_nn on all the rows of the frame excluding the one tested
    """
    confusionMatrix,names = init_confusionMatrix(df, spec)
    
    for tested in range(df.shape[0]):    
        prediction = k_nn(df, df.iloc[tested], spec, k)    
        
        
        if prediction == df.iloc[tested,-1]:
            i = names.index(prediction)
            confusionMatrix[i,i] += 1
        elif prediction != df.iloc[tested,-1]: 
            i = names.index(prediction)
            j = names.index(df.iloc[tested,-1])
            confusionMatrix[i,j] += 1
    
    print(confusionMatrix)
    print("k:" , k)
    print("accuracy: ", compute_accuracy(confusionMatrix))
    print("precision: ", compute_precision(confusionMatrix))
    print("recall: ", compute_recall(confusionMatrix))
    print("")
    
# --------------------------------------------------------------------------- #
df = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth","PetalLength","PetalWidth","Class"])
#
#k_nn_all(df, 3, "Class")
#k_nn_all(df, 5, "Class")
#k_nn_all(df, 10, "Class")
k_nn_all(df, 20, "Class")