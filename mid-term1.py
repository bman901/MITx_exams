#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:50:11 2023

@author: benkehoe
"""

def isMyNumber(guess):
    
    secretnumber = 14
    
    if guess > secretnumber:
        return 1
    elif guess == secretnumber:
        return 0
    else:
        return -1
    
def findNumber():
    guess = 1
    if isMyNumber(guess) == 1:
        return guess
    else:
        while isMyNumber(guess) != 0:
            sign = isMyNumber(guess)
            if sign == -1:
                guess *= 2
            else:
                guess -= 1
    return guess


def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    foundNumber = False

    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0:
            return guess
            foundNumber = True
        elif sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess