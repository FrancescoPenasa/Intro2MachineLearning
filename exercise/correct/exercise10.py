#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:37:19 2019

@author: manuel
"""

# Exercise 10   
# Given the iris dataset, create 3-d scatter plots in order to plot two dimensions 
# of the points against one of the other two numerical dimensions (remember 
# exercise 7? Choose the pair of dimensions you consider to be most suitable 
# for applying k-nearest neighbors). Explore the two plots; do you see any 
# relevant difference?

# Then, create a function to predict the value of the third dimensions
# using the weighted k-neighbors algorithm. Apply the algorithm to all the 
# elements of the dataset using k = {3, 5, 10} and compute the root mean square 
# (RMS) error.

# %matplotlib qt
# %matplotlib inline

import math
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

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
        distance = euclidean_distance(point, newPoint)
        # when evaluating, do not include the point to be predicted in the solution
        # (this would be cheating)
        if(distance!=0):
            distances.append((distance,frame.iloc[index,-1]))                

    distances.sort()
    
    return distances

def plot_data3d(frame, col1, col2, col3):
    """
    Print a plot of the points in the dataframe using col1 and col2.
    """    
    # print plots
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set_zlabel(col3)

    ax.plot(frame[col1], frame[col2], frame[col3], 'o')
    plt.title("3d plot")
    plt.grid(True)    
    plt.show() 

def weighted_k_nn(frame, newPoint, k, d0):
    """
    Predict the class of a point using the weighted k-nearest neighbor approach.
    """                    
    numSum = 0
    denSum = 0    
    
    # find all distances wrt the newPoint
    dist = find_distances(reducedFrame, newPoint)
    
    # find the nearest k points
    neighbors = [neighbor for neighbor in dist[:k]]    
    
    # iterate over the neighbors to compute the weighted average
    for neighbor in neighbors:
        numSum += neighbor[1] / (neighbor[0] + d0)
        denSum += 1 / (neighbor[0] + d0)
        
    prediction = numSum / denSum
    
    return prediction

def evaluate_regression(frame, k, d0):
    """
    Compute the RMS error in order to evaluate the results obtained by
    applying the weighted k-nearest neighbors algorithm.
    """    
    errors_sum = 0 
    
    # iterate over all rows of the dataframe
    for i in range(frame.shape[0]):
        
        # extract the row from the dataframe
        flower = frame.iloc[i,:]        
            
        # predict the label of each row using k-nn
        prediction = weighted_k_nn(frame, flower.tolist()[:-1], k, d0)                      
    
        # compute the sum used for defining RMS
        errors_sum += (flower[-1] - prediction)**2
        
    # compute RMS
    rms = math.sqrt(errors_sum/frame.shape[0])
    
    return rms

# -----------------------------------------------------------------------------

# read and define data
frame = pd.read_csv("/yourPathHere/iris.data", names = ["SepalLength","SepalWidth","PetalLength","PetalWidth","Class"])

# explore possible combinations for applying w-knn using %matplotlib qt
plot_data3d(frame, "PetalLength","PetalWidth","SepalWidth")
plot_data3d(frame, "PetalLength","PetalWidth","SepalLength") #

d0 = 0.01

k = 3

# filter the dataframe (remove unused dimensions), run wknn and compute RMS
reducedFrame = frame.drop(columns=["SepalWidth","Class"])
output = evaluate_regression(reducedFrame, k, d0)
print("RMS = {0:.4f}".format(output))

k = 5

# filter the dataframe (remove unused dimensions), run wknn and compute RMS
reducedFrame = frame.drop(columns=["SepalWidth","Class"])
output = evaluate_regression(reducedFrame, k, d0)
print("RMS = {0:.4f}".format(output))

k = 10

# filter the dataframe (remove unused dimensions), run wknn and compute RMS
reducedFrame = frame.drop(columns=["SepalWidth","Class"])
output = evaluate_regression(reducedFrame, k, d0)
print("RMS = {0:.4f}".format(output))