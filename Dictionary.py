# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:24:06 2018

@author: Anton
"""

# Sets are faster than list and tuples in general. Can only have one of each element in a set,
# and they are not ordered
# some methods, intersection, union, difference

student={'name': 'John', 'age': 25}
print(student.get('phone', 'not found'))
student.update({'name': 'Jane', 'age': 20})

# pop, del

for key, value in student.items():
    print(key, value)