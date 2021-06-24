# -*- coding: utf-8 -*-
"""
warmup02_string_times.py

@author: MacGuffin_

Created on Mon Jun 21 09:15:43 2021
----------------------------------------
Given a string and a non-negative int n, return a larger string that is n 
copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
def string_times(str, n):
    return str * n
