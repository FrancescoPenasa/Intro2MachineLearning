#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:37:47 2019

@author: francesco
"""

# EXERCISE 4: Given a list of 2-dimensional tuples, without using any package
#   or built-in function, define functions to (and print results):
# - find the Euclidean distance between two tuples t1 and t2
# - find the Euclidean distance between all tuples of the list
# - to compute the coordinates of the centroid of the list of tuples
#TIP: you can use the math module (use `import math`)

import math

CONST_INPUT = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0)]


def euclidean_distance(start, stop):
    """find the Euclidean distance between two tuples t1 and t2"""
    x_distance = stop[0]-start[0]
    y_distance = stop[1]-start[1]
    print("distance : ", math.sqrt(x_distance*x_distance + y_distance*y_distance))

def euclidean_distance_all(points):
    """find the Euclidean distance between all tuples of the list"""
    for start_point in points:
        for stop_point in points:
            print("point", start_point, "point", stop_point)
            euclidean_distance(start_point, stop_point)

def compute_centroid(points):
    """to compute the coordinates of the centroid of the list of tuples"""
    x_sum = 0
    y_sum = 0
    for coordinate in points:
        x_sum += coordinate[0]
        y_sum += coordinate[1]
    print("centroid : ", x_sum/len(points), y_sum/len(points))



euclidean_distance(CONST_INPUT[0], CONST_INPUT[1])
euclidean_distance_all(CONST_INPUT)
compute_centroid(CONST_INPUT)