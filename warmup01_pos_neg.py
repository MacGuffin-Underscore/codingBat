# -*- coding: utf-8 -*-
"""
warmup01_pos_neg.py

@author: MacGuffin_

Created on Mon Jun 21 08:55:10 2021
------------------------------------
Given 2 int values, return True if one is negative and one is positive. Except 
if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
    if negative:                # if negative is true
        return(a < 0 and b < 0) # returns true if both are negative
    else:                       # if negative is false
        return((a < 0 and b > 0) or (b < 0 and a > 0)) # returns true is one is neg and the other pos
