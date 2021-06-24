# -*- coding: utf-8 -*-
"""
string02_count_code.py

@author: MacGuffin_

Created on Wed Jun 23 16:43:20 2021
----------------------------------------
Return the number of times that the string "code" appears anywhere in the 
given string, except we'll accept any letter for the 'd', so "cope" and "cooe" 
count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2]+str[i+3] == "coe":
            count += 1
    return count
