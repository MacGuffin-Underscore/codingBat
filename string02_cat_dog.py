# -*- coding: utf-8 -*-
"""
string02_cat_dog.py

@author: MacGuffin_

Created on Wed Jun 23 16:16:46 2021
----------------------------------------
Return True if the string "cat" and "dog" appear the same number of times in 
the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str)-2):
        if str[i]+str[i+1]+str[i+2] == "cat":
            cat += 1
        elif str[i]+str[i+1]+str[i+2] == 'dog':
            dog += 1
    return cat == dog