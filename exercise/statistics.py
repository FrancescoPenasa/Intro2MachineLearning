#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:30:25 2019

@author: francesco
"""


import math
import numpy as np

def expected_value(X_values, X_probabilities):
    """
    SUM(x*p)
    """
    if len(X_values) != len(X_probabilities):
        return -1
    else:
        mean = 0
        for i in range(len(X_values)):
            mean += X_values[i] * X_probabilities[i]
        return mean
    
def variance(X):
    """
    VAR(X) = SUM[(xi - E(X))^2 * pi]
    VAR(X) = SUM[xi^2 * pi] - E(X)^2
    """
    values = X[0]
    probabilities = X[1]
    variance = 0
    mean = expected_value(X[0], X[1])

    for i in range(len(values)):
        variance += math.pow((values[i] - mean), 2) * probabilities[i]
    
    # method 2
    variance2 = 0
    for i in range(len(values)):
        variance2 += math.pow(values[i], 2) * probabilities[i] 
    variance2 -= mean*mean
    
    print(variance)    
    print(variance2)    
    
    
def covarianza(X_values, X_probabilities, Y_values, Y_probabilities):
    """
    cov(X,Y) = E[(X - E[X])(Y - E[Y])]
    """
    X_mean = expected_value(X_values, X_probabilities)
    Y_mean = expected_value(Y_values, Y_probabilities)
    
    part = 0
    for i in range(len(X_values)):
        part += (X_values[i] - X_mean) * (Y_values[i] - Y_mean)
    
    
    coVariance = part/(len(X_values)-1)
    print (coVariance)
    
#x[0] values x[1]probability
X = [2.1,2.5,3.6,4.0], [1/4, 1/4, 1/4, 1/4]
Y = [8,10,12,14], [1/4, 1/4, 1/4, 1/4]
covarianza(X[0],X[1],Y[0],Y[1])
variance(X)
mean = expected_value(X[0], X[1])
print(mean)
