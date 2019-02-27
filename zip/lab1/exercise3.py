#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:24:46 2019

@author: manuel
"""

# EXERCISE 3:
# Given a list of numbers, without using any package or built-in function:
# - define a function to swap the values of two elements in the list
# - define a function to order ascendently the list
# - find mean and median

list = [30,10,40,20,50]

def swap(local_list, pos1, pos2):
    temp = local_list[pos1]
    local_list[pos1] = local_list[pos2]
    local_list[pos2] = temp

def order(local_list):
    for id1,element1 in enumerate(local_list):
        for id2,element2 in enumerate(local_list):
            if element1 < element2:
                swap(local_list,id1,id2)
                
def find_median(local_list):
    list_size = len(local_list)
    
    if(list_size % 2 == 0):
        median = local_list[list_size // 2 + 1]
    else: 
        median = local_list[list_size // 2]
        
    return median

def find_mean(local_list):
    list_size = len(local_list)
    tmp_sum = 0
    
    for i in local_list:
        tmp_sum += tmp_sum + i
        
    return tmp_sum / list_size

print("Unordered list:", list)
order(list)
print("Ordered list:", list)

median = find_median(list)
print("The median is", median)

mean = find_mean(list)
print("The mean is", mean)
