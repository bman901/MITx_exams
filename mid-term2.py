#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:02:04 2023

@author: benkehoe
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    count = 0
    
    while count < len(L)//2:
        L[count], L[len(L)-(count+1)] = L[len(L)-(count+1)],L[count]
        count += 1
    
    for item in L:
        count_item = 0
        while count_item < len(item)//2:
            item[count_item], item[len(item)-(count_item+1)] = item[len(item)-(count_item+1)],item[count_item]
            count_item += 1
