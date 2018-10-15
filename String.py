# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:55:00 2018

@author: Anton
"""

message="""Hello
world"""
print(message)
print(message[0])
print(message[0:5]) # from first to (5-1) th value. Called slicing
print(message.find("Hello")) # starts at this index
print(message.find("Hi")) # gives -1 if it does not exist
message=message.replace("world", "Universe")
print(message)
message= "{}, {}. Welcome!".format("Anton", "Backstrom")
print(message)
str1="Anton"
str2="Backstrom"
message= f"{str1}, {str2}. Welcome!"
print(message)