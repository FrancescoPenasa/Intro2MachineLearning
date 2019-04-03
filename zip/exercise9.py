#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:22:08 2019

@author: manuel
"""

# Exercise 9
# Given the iris dataset CSV file, apply the k-nearest neighbors algorithm to 
# all the elements of the dataset using k = {3, 5, 10, 20} and build the confusion
# matrix. Also, compute total precision, total accuracy and total recall.

import pandas as pd
import math
import numpy as np

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

def build_confusion_matrix_knn(dataframe, colClassString, k):
    """
    Build the confusion matrix obtained by classifying all points in the dataframe
    using the k-nearest neighbor algorithm.
    """        
    # get list and number of the unique classes to initialize the confusion matrix
    classes = dataframe[colClassString].unique()      
    classes_number = len(classes)
    confusion_matrix = np.zeros((classes_number, classes_number))
    
    # iterate over all rows of the dataframe
    for i in range(dataframe.shape[0]):     
        
        # extract each row from the dataframe
        flower = dataframe.iloc[i,:]
        
        # predict the label using k-nn
        prediction = k_nn(dataframe, flower.tolist()[:-1], colClassString, k)
    
        # get the row of the cell to update (where is classes = class_label? )
        row_index_ground_truth = np.where(classes==flower[-1])
        
        # get the column of the cell to update (where is classes = prediction? )
        col_index_classification = np.where(classes==prediction)  
        
        # update the count in the right cell of the confusion matrix
        confusion_matrix[row_index_ground_truth,col_index_classification] += 1
        
    return confusion_matrix

def precision(label_index, confusion_matrix):
    """
    Compute the precision of the class corresponding to label_index, using a
    confusion matrix.
    """
    # get the false positives (column of the confusion matrix) of a class
    col = confusion_matrix[:, label_index]
    fp = col.sum()
    
    # get the true positives (element on the diagonal) of a class
    tp = confusion_matrix[label_index, label_index]
        
    precision = tp / fp    
    return precision
    
def recall(label_index, confusion_matrix):
    """
    Compute the recall of the class corresponding to label_index, using a
    confusion matrix.
    """        
    # get the false negatives (row of the confusion matrix) of a class
    row = confusion_matrix[label_index, :]
    fn = row.sum()
    
    # get the true positives (element on the diagonal) of a class
    tp = confusion_matrix[label_index, label_index]    
        
    recall = tp / fn
    return recall    

def total_accuracy(confusion_matrix):
    """
    Compute the total accuracy of all the classes in the confusion matrix.
    """        
    # compute average accuracy of all classes
    diagonal_sum = confusion_matrix.trace()
    matrix_sum = confusion_matrix.sum()
    
    total_accuracy = diagonal_sum / matrix_sum
    return total_accuracy

def total_precision(confusion_matrix):
    """
    Compute the total precision of all the classes in the confusion matrix.
    """        
    rows, columns = confusion_matrix.shape
    tmpsum = 0
    
    # compute average precision of all classes
    for label_index in range(rows):
        tmpsum += precision(label_index, confusion_matrix)
        
    total_precision = tmpsum / rows
    return total_precision

def total_recall(confusion_matrix):
    """
    Compute the total recall of all the classes in the confusion matrix.
    """        
    rows, columns = confusion_matrix.shape
    tmpsum = 0
    
    # compute average recall of all classes
    for label in range(columns):
        tmpsum += recall(label, confusion_matrix)
        
    total_recall = tmpsum / columns
    return total_recall

# -----------------------------------------------------------------------------

# read and define data
frame = pd.read_csv("/yourPathHere/iris.data", names = ["SepalLength","SepalWidth","PetalLength","PetalWidth","Class"])

k = 3
cm = build_confusion_matrix_knn(frame, "Class", k)
total_acc = total_accuracy(cm)
total_pre = total_precision(cm)
total_rec = total_recall(cm)
tmpString = "{0:.2f}"
print("Using k =", k, ": Total accuracy =", tmpString.format(total_acc),
      "Total precision =", tmpString.format(total_pre),
      "Total recall =", tmpString.format(total_rec))

k = 5
cm = build_confusion_matrix_knn(frame, "Class", k)
total_acc = total_accuracy(cm)
total_pre = total_precision(cm)
total_rec = total_recall(cm)
tmpString = "{0:.2f}"
print("Using k =", k, ": Total accuracy =", tmpString.format(total_acc),
      "Total precision =", tmpString.format(total_pre),
      "Total recall =", tmpString.format(total_rec))

k = 10
cm = build_confusion_matrix_knn(frame, "Class", k)
total_acc = total_accuracy(cm)
total_pre = total_precision(cm)
total_rec = total_recall(cm)
tmpString = "{0:.2f}"
print("Using k =", k, ": Total accuracy =", tmpString.format(total_acc),
      "Total precision =", tmpString.format(total_pre),
      "Total recall =", tmpString.format(total_rec))

k = 20
cm = build_confusion_matrix_knn(frame, "Class", k)
total_acc = total_accuracy(cm)
total_pre = total_precision(cm)
total_rec = total_recall(cm)
tmpString = "{0:.2f}"
print("Using k =", k, ": Total accuracy =", tmpString.format(total_acc),
      "Total precision =", tmpString.format(total_pre),
      "Total recall =", tmpString.format(total_rec))