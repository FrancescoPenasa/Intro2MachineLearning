#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:44:31 2019

@author: manuel
"""

# Exercise 14
# Given the iris dataset, apply PCA with k=2 and plot projected data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
path = "iris.data"
df = pd.read_csv(path)

# extract only input dimensions from data
A = df.iloc[:,0:4].values

# standardize data (subtract mean and divide by standard deviation of columns)
M = np.mean(A.T, axis=1)
S = np.std(A.T, axis=1) 
N = (A - M)/S

# compute covariance matrix of data (must be dXd, where d = original dimension)
V = np.cov(N.T)

# compute eigendecomposition of covariance matrix (must obtain d eigenvectors)
eig_vals, eig_vecs = np.linalg.eig(V)

# sort eigenvalues and eigenvectors according to eigenvalues
idx = np.argsort(eig_vals)[::-1] # find the indexes which sort the array (reverse)
eig_vecs = eig_vecs[:,idx]
eig_vals = eig_vals[idx]

# extract first two eigenvectors (transpose because eigenvectors are columns here)
projection_vectors = np.array([eig_vecs.T[0], eig_vecs.T[1]])

# project standardized data (must obtain nX2, where n = number of data points)
P = np.dot(N, projection_vectors.T)

# plot projected data
plt.scatter(P[:,0], P[:,1])
plt.grid()
plt.show()