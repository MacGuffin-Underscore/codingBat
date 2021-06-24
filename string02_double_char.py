# -*- coding: utf-8 -*-
"""
string02_double_char.py

@author: MacGuffin_

Created on Wed Jun 23 14:42:08 2021
----------------------------------------
Given a string, return a string where for every char in the original, there 
are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""
def double_char(str):
    OUT = ''
    for i in range(len(str)):
        OUT += str[i]*2
    return OUT
        
