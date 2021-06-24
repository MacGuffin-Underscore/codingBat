# -*- coding: utf-8 -*-
"""
logic01_cigar_party.py

@author: MacGuffin_

Created on Mon Jun 21 13:23:10 2021
----------------------------------------
When squirrels get together for a party, they like to have cigars. A squirrel 
party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number 
of cigars. Return True if the party with the given values is successful, or 
False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
def cigar_party(cigars, is_weekend):
    return (cigars >= 40) and (cigars <= 60 or is_weekend)
