# -*- coding: utf-8 -*-
"""
string02_count_hi.py

@author: MacGuffin_

Created on Wed Jun 23 16:40:10 2021
----------------------------------------
Return the number of times that the string "hi" appears anywhere in the given 
string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
def count_hi(str):
    OUT = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            OUT += 2
    return OUT