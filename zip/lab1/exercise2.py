#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:12:09 2019

@author: manuel
"""

# EXERCISE 2:
# Given a list of integers, without using any package or built-in function, compute and print:
# - a dictionary where keys are unique numbers contained in the list, and
#   values count the occurrencies of unique numbers in the list
# TIP: you can use dictionary functions

list = [1,2,3,4,2,3,1,2,3,4,2,1,3]

dict_counter = {}

for i in list:
    value = dict_counter.get(i)
    if value == None:
        value = 0
    dict_counter.update({i: value + 1})

print("The occurrencies which have been found are:\n", dict_counter)
