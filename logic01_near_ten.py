# -*- coding: utf-8 -*-
"""
logic01_near_ten.py

@author: MacGuffin_

Created on Mon Jun 21 15:25:51 2021
----------------------------------------
Given a non-negative number "num", return True if num is within 2 of a 
multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) 
is 2.

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""
def near_ten(num):
    rng = [0,1,2,8,9]
    return num % 10 in rng
