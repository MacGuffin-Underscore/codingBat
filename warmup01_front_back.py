# -*- coding: utf-8 -*-
"""
warmup01_front_back.py

@author: MacGuffin_

Created on Mon Jun 21 07:49:36 2021
------------------------------------
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]

print(front_back("ab"))