# -*- coding: utf-8 -*-
"""
string01_first_half.py

@author: MacGuffin_

Created on Mon Jun 21 10:50:30 2021
----------------------------------------
Given a string of even length, return the first half. So the string "WooHoo" 
yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""
def first_half(str):
    return str[:len(str)/2]
