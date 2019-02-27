#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:24:46 2019

@author: manuel
"""

# EXERCISE 1:
# Given a list of integers, without using any package or built-in function, compute and print:
# - mean of the list
# - number of negative and positive numbers in the list
# - two lists that contain positives and negatives in the original list

list = [-2,2,-3,3,10]

sum = 0
positives = 0
negatives = 0
pos_list = []
neg_list = []

for i in list:
    sum =+ i
    if(i>0):
        positives += 1
        pos_list.append(i)
    elif(i<0): 
        negatives += 1
        neg_list.append(i)
    
mean = sum / len(list)

print("The mean is",mean)
print("The number of positives is", positives)
print("The number of negatives is", negatives)
print("The list of found positives is", pos_list)
print("The list of found negatives is", neg_list)
