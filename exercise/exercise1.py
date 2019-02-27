#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:59:26 2019

@author: francesco
"""
# EXERCISE 1:
#Given a list of integers, without using any package or built-in function, compute and print:
# - mean of the list
# - number of negative and positive numbers in the list
# - two lists that contain positives and negatives in the original list

input = [-2,2,-3,3,10]


# - mean of the list
tot = 0;
for n in input:
    tot += n
print("Mean = ", tot/len(input))


# - number of negative and positive numbers in the list
positive = negative = 0
for n in input:
    if n >= 0:
        positive += 1
    else:
        negative += 1
print("Positive numbers: ", positive)        
print("Negative numbers: ", negative)
    

# - two lists that contain positives and negatives in the original list
positive = []
negative = []
for n in input:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)
print("positive list: ", positive)
print("negative list: ", negative)