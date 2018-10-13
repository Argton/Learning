# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:57:34 2018

@author: Anton
"""

# Print fibonacci sequence from 0-9
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b
    

# Print fibonacci sequence from 0-9    
def fib(num):    
    a, b = 0, 1
    for i in range(0, 10):
        yield "{}: {}".format(i+1, a) # Yield is used in generators
        a, b = b, a + b
        
for item in fib(10):
    print(item)
    
    