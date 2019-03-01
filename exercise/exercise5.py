#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:52:00 2019
@author: francesco

Given a 1-dimensional vector v with n rows and a 2-dimensional matrix M with n columns, 
without using any built-in function, define functions to:
 - compute the inner product of two vectors v1 and v2
 - compute the product of x and M
 
TIP: you can use Python lists
"""

import numpy as np
#help(np)
#help(np.linalg)
v = np.array([2,1,3])
M = np.array([[1,2,3],[4,5,6],[7,8,9]])

def inner_product(v1, v2):
    """compute the inner product of two vectors v1 and v2"""
    v1 = np.matrix(v1)
    v2 = np.matrix(v2)
    print ("Inner product: ", v1*v2)
    
def product(v, M):
    """compute the product of x and M"""
    inner_product(v, M)
    
product(v, M)


####other way
if v.shape[0] == v.size:
    res = np.zeros((1,M.shape[0]))
else:
    res = np.zeros((v.shape[1],M.shape[0]))
    
    
for column in range(v.shape[0]):
    for j in range(M.shape[0]):
        res[0][column] += v[j]*M[j][column]

print(res)