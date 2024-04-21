#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:50:28 2023

@author: benkehoe
"""

#Write a Python function that returns a list of keys in aDict that map to
#integer values that are unique (i.e. values appear exactly once in aDict).
#The list of keys you return should be sorted in increasing order.

#(If aDict does not contain any unique values, you should return an empty list.)

#This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    
    values = aDict.values()
    store = []
    duplicates = []
    keys = []
    
    for check in values:
        if check not in store:
            store.append(check)
        else:
            duplicates.append(check)
    
    for check in duplicates:
        if check in store:
            store.remove(check)
        
    
    for check in aDict:
        if aDict[check] in store:
            keys.append(check)
    
    sortedkeys = sorted(keys)
    
    return sortedkeys