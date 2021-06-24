# -*- coding: utf-8 -*-
"""
string01_make_tags.py

@author: MacGuffin_

Created on Mon Jun 21 10:34:05 2021
----------------------------------------
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as 
italic text. In this example, the "i" tag makes <i> and </i> which surround 
the word "Yay". Given tag and word strings, create the HTML string with tags 
around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""
def make_tags(tag, word):
    return '<'+tag+'>'+word+'</'+tag+'>'
