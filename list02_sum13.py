# -*- coding: utf-8 -*-
"""
list02_sum13.py

@author: MacGuffin_

Created on Wed Jun 23 18:47:38 2021
----------------------------------------
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""
def sum13(nums):
    skip = False
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            skip = True
        if not skip:
            sum += nums[i]
        if nums[i] != 13:
            skip = False
        
    return sum
        
