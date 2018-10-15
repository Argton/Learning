# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:29:24 2018

@author: Anton
"""

# LEGB: Local, Enclosing, Global, Built-in

x = 'global x'
s = 'local'

def test():
    y = 'local y'
    global s # overwrites
    
print(s)
    
    