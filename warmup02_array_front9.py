# -*- coding: utf-8 -*-
"""
warmup02_array_front9.py

@author: MacGuffin_

Created on Mon Jun 21 09:29:25 2021
----------------------------------------
Given an array of ints, return True if one of the first 4 elements in the 
array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
    # This if statement shortens the check if the array is shorter than 4
    if len(nums) < 4: n = len(nums)
    else: n = 4
        
    for i in range(n):
        if nums[i] == 9:
            return True
    return False

print(array_front9([1,2,9]))