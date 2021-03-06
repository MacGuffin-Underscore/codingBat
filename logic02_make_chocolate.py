# -*- coding: utf-8 -*-
"""
logic02_make_chocolate.py

@author: MacGuffin_

Created on Wed Jun 23 14:34:52 2021
----------------------------------------
We want make a package of goal kilos of chocolate. We have small bars (1 kilo 
each) and big bars (5 kilos each). Return the number of small bars to use, 
assuming we always use big bars before small bars. Return -1 if it can't be 
done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""
def make_chocolate(small, big, goal):
    [bb, sb] = divmod(goal,5)
    if big < bb:
        sb += (bb - big)*5
    if small < sb:
        return -1
    return sb
