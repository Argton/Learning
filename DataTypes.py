# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:38:53 2018

@author: Anton
"""

my_list = [1,2,3,4]
for i in my_list:
    print(i)
    
print("\n")
    
for i in range(0,len(my_list)):
    print(my_list[i])
    
my_tuple = (1,2,3,4)


my_dict={'name': 'Anton', 'age': '31'}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('name'))
    
my_set = {1,2,3,4}

squares=[num*num for num in my_list] # List comprehension
print(squares)