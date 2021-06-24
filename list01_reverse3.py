# -*- coding: utf-8 -*-
"""
list01_reverse3.py

@author: MacGuffin_

Created on Mon Jun 21 12:46:59 2021
----------------------------------------
Given an array of ints length 3, return a new array with the elements in 
reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]
