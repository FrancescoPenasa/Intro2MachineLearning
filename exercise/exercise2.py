#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:59:26 2019

@author: francesco
"""

# EXERCISE 2:
# Given a list of integers, without using any package or built-in function, compute and print:
# - a dictionary where:
# - keys are unique numbers contained in the list
# - values count the occurrencies of unique numbers in the list
#TIP: you can use dictionary functions

input = [1,2,3,4,2,3,1,2,3,4,2,1,3]


# - a dictionary where:
dict = {}

for n in input:
    if n in dict.keys():    #keys are unique numbers contained in the list
        dict[n] += 1
    else:                   #values count the occurrencies of unique numbers in the list
        dict[n] = 1
        
print("Dict: ", dict)