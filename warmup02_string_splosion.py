# -*- coding: utf-8 -*-
"""
warmup02_string_splosion.py

@author: MacGuffin_

Created on Mon Jun 21 10:24:59 2021
----------------------------------------
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
    OUT = ''
    for i in range(len(str)):
        OUT += str[:i+1]
    return OUT

print(string_splosion('code'))
