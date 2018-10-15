# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:36:56 2018

@author: Anton
"""

import os
from datetime import datetime

print(os.getcwd())
print(os.__file__)
#print(dir(os))
print(os.listdir())
print(os.environ.get("HOME"))
print(os.path.exists("textfile.txt"))
os.mkdir("New") # Or makedirs for making subdirectories
os.rmdir("New")

#os.stat("filename.txt") #.st_size, st_mtime after
#os.rmdir("New") # doesn't work for some reason
#print(datetime.fromtimestamp("textfile.txt")
#os.walk("/location") # gives directories, subdirectories and files in specified location


os.chdir("/Users")
print(os.getcwd())
# for f in os.listdir():
# f_name, f_ext = os.path.splitext(f)
# f_title, f_num = f_title.split('-')
# f_title = f_title.strip()
# f_num = f_num.strip()[1:].zfill(2)
# os.rename(name, newname)