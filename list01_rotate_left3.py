# -*- coding: utf-8 -*-
"""
list01_rotate_left3.py

@author: MacGuffin_

Created on Mon Jun 21 13:01:23 2021
----------------------------------------
Given an array of ints length 3, return an array with the elements "rotated 
left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""
def rotate_left3(nums):
    hold = nums[0]
    nums[0] = nums[1]
    nums[1] = nums[2]
    nums[2] = hold
    return nums
