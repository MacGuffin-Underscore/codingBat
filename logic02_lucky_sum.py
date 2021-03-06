# -*- coding: utf-8 -*-
"""
logic02_lucky_sum.py

@author: MacGuffin_

Created on Wed Jun 23 13:09:50 2021
----------------------------------------
Given 3 int values, a b c, return their sum. However, if one of the values is 
13 then it does not count towards the sum and values to its right do not 
count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
def lucky_sum(a, b, c):
    sum = 0
    if a != 13: sum += a
    else: return sum
    if b != 13: sum += b
    else: return sum
    if c != 13: sum += c
    return sum
    
