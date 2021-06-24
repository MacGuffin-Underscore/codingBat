# -*- coding: utf-8 -*-
"""
logic01_love6.py

@author: MacGuffin_

Created on Mon Jun 21 15:35:08 2021
----------------------------------------
The number 6 is a truly great number. Given two int values, a and b, return 
True if either one is 6. Or if their sum or difference is 6. Note: the 
function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""
def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6
        
