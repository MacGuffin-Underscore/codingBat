# -*- coding: utf-8 -*-
"""
string01_without_end.py

@author: MacGuffin_

Created on Mon Jun 21 10:44:09 2021
----------------------------------------
Given a string, return a version without the first and last char, so "Hello" 
yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""
def without_end(str):
    if len(str)<3: return ''
    return str[1:len(str)-1]
