# -*- coding: utf-8 -*-
"""
list01_same_first_last.py

@author: MacGuffin_

Created on Mon Jun 21 12:55:18 2021
----------------------------------------
Given an array of ints, return True if the array is length 1 or more, and the 
first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
def same_first_last(nums):
    return (len(nums) > 1) and (nums[0] == nums[-1]) or len(nums) == 1
