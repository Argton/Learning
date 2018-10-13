# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:50:23 2018

@author: Anton
"""

import os, glob

a = 10;
b = 20;

print("{} is less than {}".format(a,b)) # formatting data

os.chdir("/Users/Anton/Desktop/Code/Python/Learning")
for file in glob.glob("*.jpg"):
    print(file) # prints name of all file containing ".jpg"
    
    
