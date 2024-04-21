#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:20:10 2023

@author: benkehoe
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    # L1 = [1, 2, 1]
    # L2 = [1, 2, 1]
    
    L2_copy = L2[:]
    highest_dict = {}
    
    if len(L1) != len(L2):
        return False
    
    for n in L1:
        if n in L2_copy:
            if n in highest_dict.keys():
                highest_dict[n] += 1
            else:
                highest_dict[n] = 1
                
            L2_copy.remove(n)
        else:
            return False
            break
    
    if not False:
        if highest_dict == {}:
            high = None
            key = None
        else:
            high = max(highest_dict.values())
            for n in highest_dict:
                if highest_dict[n] == high:
                    key = n
                    break
        
        return (key, high, type(key))
    