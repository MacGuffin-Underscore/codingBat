# -*- coding: utf-8 -*-
"""
logic02_make_bricks.py

@author: MacGuffin_

Created on Mon Jun 21 15:42:27 2021
----------------------------------------
We want to make a row of bricks that is EXACTLY goal inches long. We have a 
number of small bricks (1 inch each) and big bricks (5 inches each). Return 
True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""
def make_bricks(small, big, goal):
    [bb, sb] = divmod(goal,5)
    if big < bb:
        sb += (bb - big)*5
    return small >= sb
