# -*- coding: utf-8 -*-
"""
string02_xyz_there.py

@author: MacGuffin_

Created on Wed Jun 23 16:47:00 2021
----------------------------------------
Return True if the given string contains an appearance of "xyz" where the xyz 
is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does 
not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):
    for i in range(len(str)-2):
        if str[i-1] != '.' and str[i:i+3] == 'xyz':
            return True 
    return False