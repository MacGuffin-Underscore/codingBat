# -*- coding: utf-8 -*-
"""
warmup02_string_bits.py

@author: MacGuffin_

Created on Mon Jun 21 09:52:17 2021
----------------------------------------
Given a string, return a new string made of every other char starting with 
the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
    OUT = ''
    for i in range(len(str)):
        if i % 2 == 0:
            OUT += str[i]
    return OUT
        

