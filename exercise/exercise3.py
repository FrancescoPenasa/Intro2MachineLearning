#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:37:34 2019

@author: francesco
"""


#EXERCISE 3:
#Given an unordered list of numbers, without using any package or built-in function, define functions to (and print results):
#
#swap the values of two elements in the list
#order ascendently the list
#find mean and median of the lis

input = [30,10,40,20,50]

#swap the values of two elements in the list
def swap(list, x, y):
    """swap two elements of a list"""
    index_x = list.index(x)
    index_y = list.index(y)
    list[index_x] = y
    list[index_y] = x    
    

#order ascendently the list
def sort_ascendently(list):
    """sort a list and reverse it"""
    list.sort();
    list.reverse();
    

#find mean and median of the lis
def find_mean(list):
    """find the mean in a list"""
    tot = 0
    for n in list:
        tot += n
    return tot/len(list)

def find_median(list):
    """find the median in a list"""
    if(len(list) % 2 == 0):
        median_index = len(list)//2 + 1 
    else:
        median_index = len(list)//2
    return list[median_index]

#swap the values of two elements in the list
print(input)
swap(input, 10, 40)
print(input)   


#order ascendently the list    
print(input)   
sort_ascendently(input)
print(input)   

    
#find mean and median of the lis
print(input)
print(find_mean(input))
print(find_median(input))
