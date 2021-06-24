# -*- coding: utf-8 -*-
"""
string01_non_start.py

@author: MacGuffin_

Created on Mon Jun 21 10:48:33 2021
----------------------------------------
Given 2 strings, return their concatenation, except omit the first char of 
each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""
def non_start(a, b):
    return a[1:]+b[1:]