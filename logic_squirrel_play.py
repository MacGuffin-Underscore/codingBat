# -*- coding: utf-8 -*-
"""
logic_squirrel_play.py

@author: MacGuffin_

Created on Mon Jun 21 15:19:57 2021
----------------------------------------
The squirrels in Palo Alto spend most of the day playing. In particular, they 
play if the temperature is between 60 and 90 (inclusive). Unless it is summer, 
then the upper limit is 100 instead of 90. Given an int temperature and a 
boolean is_summer, return True if the squirrels play and False otherwise.

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""
def squirrel_play(temp, is_summer):
    limit = [60,90]
    if is_summer:
        limit[1] = 100
    return limit[0] <= temp <= limit[1]
