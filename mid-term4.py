#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:51:05 2023

@author: benkehoe
"""

#Write a recursive Python function, given a non-negative integer N,
#to calculate and return the sum of its digits.

#Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6)
#while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

#This function has to be recursive; you may not use loops!

#This function takes in one integer and returns one integer.

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N//10 == 0:
        return N
    else:
        return N%10 + sumDigits(N//10)