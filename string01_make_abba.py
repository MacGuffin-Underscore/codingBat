# -*- coding: utf-8 -*-
"""
string01_make_abba.py

@author: MacGuffin_

Created on Mon Jun 21 10:40:08 2021
----------------------------------------
Given two strings, a and b, return the result of putting them together in the 
order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""
def make_abba(a, b):
    return a+b+b+a
