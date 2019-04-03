#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:43:23 2019

@author: francesco

Given the iris dataset, create 3-d scatter plots in order to plot two dimensions 
of the points against one of the other two numerical dimensions 
(remember exercise 7? Choose the pair of dimensions you consider to be most suitable for applying k-nearest neighbors). 
Explore the two plots; do you see any relevant difference?

Then, create a function to predict the value of the third dimensions using 
the weighted k-neighbors algorithm. Apply the algorithm to all the elements 
of the dataset using k = {3, 5, 10} and compute the root mean square (RMS) error.

TIPS:
- to explore the plots, remember from the Spider tutorial that you can use 
%matplotlib qt and %matplotlib inline commands to switch 
between interactive and inline visualization modes

- when evaluating, do not include the point you are predicting in the neighbors 
(this would be cheating)
"""

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import sys

def euclidean_distance(s1,s2):
    """
    Compute the Euclidean distance between two n-dimensional objects.
    """    
    tmpsum = 0
    
    for index,value in enumerate(s1):
        tmpsum += (s1[index]-s2[index])**2
    
    return math.sqrt(tmpsum)

def find_distances(frame, newPoint, weigth):
    """
    Find the distance between a point and all the points in a dataframe, and
    sort the elements in ascending order.
    """                
    distances = []    
    weigth = frame.columns.get_loc(weigth)
    for index in range(frame.shape[0]):

        # get all columns of a row (except the label) 
        point = frame.iloc[index,:-1]        

    	# compute the distance, then save distance and label 
        # (use distance as first value)
        distance = euclidean_distance(point, newPoint)
        
        if distance != 0:
            distances.append((distance, frame.iloc[index,-1], frame.iloc[index, weigth]))                
        else:
            distances.append((sys.maxsize, frame.iloc[index,-1], frame.iloc[index, weigth]))                
            
    distances.sort()
    return distances


def wk_nn(frame, newPoint, weigth, colClass, k):
    """
    Predict the class of a point by using the k-nearest neighbor algorithm on 
    the points of a dataframe.
    """                
    num = {"Iris-virginica":0,
           "Iris-versicolor":0,
           "Iris-setosa":0}
    denum = 0
    d0 = 1

    # find all distances wrt the newPoint
    dist = find_distances(frame, newPoint, weigth) #distance, colClass, weigth
    
    # find the nearest k points, extract their labels and save them in a list
    labels = [label for distance,label,w in dist[:k]] 
    weigths= [w for distance,label,w in dist[:k]] 
    
    for i in range(len(weigths)):
        num[labels[i]] += 1 / ((weigths[i]) + d0)
        denum += 1 / ((weigths[i]) + d0)
    
    
    mx = 0
    for label in frame[colClass].unique():
        if (num[label]/denum) > mx:
            mx = num[label]/denum
            prediction = label
        
    print("prediction: ", prediction)
    print("likelihood: ", mx)
    return(prediction)

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

def wknn_all(df, weight, spec, k):
    # truePositive, falsePositive, falseNegative, trueNegative
    confusionMatrix,names = init_confusionMatrix(df, spec)
    
    
    for tested in range(df.shape[0]):
        print("test: ",df.iloc[tested, -1])
        prediction = wk_nn(df, df.iloc[tested], weight, spec, k)    
        
        if prediction == df.iloc[tested,-1]:
            i = names.index(prediction)
            confusionMatrix[i,i] += 1
        elif prediction != df.iloc[tested,-1]: 
            i = names.index(prediction)
            j = names.index(df.iloc[tested,-1])
            confusionMatrix[i,j] += 1
    
    print(confusionMatrix)


### PRINT FUNCTION ###
def colored_plot_3D(frame, axis, colorMap):
    """
    Plot the frame with different label based on the string colorMap.
    """       
    x_label = axis[0]
    y_label = axis[1]
    z_label = axis[2]
        
    
    # create the figure
    fig = plt.figure(figsize=(15,5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    
    
    for pattern in frame[colorMap].unique():
        mask = (frame[colorMap] == pattern)
        points = frame[mask]    
        x = points[x_label]
        y = points[y_label]
        z = points[z_label]
        ax.scatter(x, y, z, c=None, depthshade=True, label=pattern)
        
    ax.grid(True)
    plt.legend()
    fig.tight_layout()

    
    

# -----------------------------------------------------------------------------

# read and define data
frame = pd.read_csv("iris.data", names = ["SepalLength","SepalWidth","PetalLength","PetalWidth","Class"])
#newFlower = [5.8, 3.0, 4.9, 1.6]
#colored_plot_3D(frame, ["PetalLength","PetalWidth","SepalLength"], "Class")
#colored_plot_3D(frame, ["PetalLength","PetalWidth","SepalWidth"], "Class")  #better one

wknn_all(frame, "PetalLength", "Class", 20)
wknn_all(frame, "PetalWidth", "Class", 20)
