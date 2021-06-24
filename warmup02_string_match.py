# -*- coding: utf-8 -*-
"""
warmup02_string_match.py

@author: MacGuffin_

Created on Mon Jun 21 10:20:02 2021
----------------------------------------
Given 2 strings, a and b, return the number of the positions where they 
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
since the "xx", "aa", and "az" substrings appear in the same place in both 
strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
    count = 0
    if len(a) < len(b): n = len(a)
    else: n = len(b)
    
    for i in range(n-1):
        if a[i]+a[i+1] == b[i]+b[i+1]:
            count += 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))