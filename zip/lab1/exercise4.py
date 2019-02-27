#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:12:09 2019

@author: manuel
"""

# EXERCISE 4:
# Given a list of 2-dimensional tuples:
# - define a function to find the Euclidean distance between t1 and t2
# - define a function to find the Euclidean distance between all elements of a Tuple list
# - define a function to compute the coordinates of the centroid of the list of points
# TIP: you can use the math module

import math

list = [(1.0,1.0), (2.0,2.0), (3.0,3.0), (4.0,4.0)]

def euclidean_distance(t1,t2):
    return math.sqrt( ((t1[0]-t2[0])**2)+((t1[1]-t2[1])**2) )

def compute_distances(tmp_list):    
    for id1,i in enumerate(tmp_list):
        for id2,j in enumerate(tmp_list):
            distance = euclidean_distance(tmp_list[id1],tmp_list[id2])
            print("The euclidean distance between", i, j, "is", "{0:.4f}".format(distance))            
        print("\n")
        
compute_distances(list)

def compute_centroid(tmp_list):
    sumx = 0
    sumy = 0
    
    for i in tmp_list:
        sumx += i[0]
        sumy += i[1]
        
    x = sumx / len(tmp_list)
    y = sumy / len(tmp_list)
    centroid = (x,y)
        
    print("The centroid of the list of points is", centroid)
        
compute_centroid(list)
