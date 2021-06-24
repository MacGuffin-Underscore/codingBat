# -*- coding: utf-8 -*-
"""
string01_extra_end.py

@author: MacGuffin_

Created on Mon Jun 21 11:06:47 2021
----------------------------------------
Given a string, return a new string made of 3 copies of the last 2 chars of 
the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""
def extra_end(str):
    return str[len(str)-2:]*3
