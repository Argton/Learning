# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:38:36 2018

@author: Anton
"""

li = [1,4,7,3,7,3,56,8,5]
s_li = sorted(li) # change old
s_li2 = sorted(li, key=abs)
li2 = li.sort() # new
# reverse=True

tup = (2,3,5,2,1,3,5)
s_tup = sorter(sup) # doesn't have sort() method

# sorted(di) works on dictionaries, sorts keys

# sort dictionaries or lists of objects: make a function dict_sort that returns the
# key you want, then do sorted(dict, key=dict_sort) 
# can have key=lambda e: e.name for instance
# or from operator import attrgetter
# key = attrgetter("key"), where key is the key you want

