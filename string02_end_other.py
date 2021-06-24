# -*- coding: utf-8 -*-
"""
string02_end_other.py

@author: MacGuffin_

Created on Wed Jun 23 16:30:01 2021
----------------------------------------
Given two strings, return True if either of the strings appears at the very 
end of the other string, ignoring upper/lower case differences (in other words, 
the computation should not be "case sensitive"). Note: s.lower() returns the 
lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""
def end_other(a, b):
    if len(a) < len(b): end = a.lower(); str = b.lower()
    else: end = b.lower(); str = a.lower()
    
    return str[len(str)-len(end):] == end
        
    
