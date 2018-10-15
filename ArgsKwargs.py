# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:42:48 2018

@author: Anton
"""

def student_info(*args, **kwargs): # takes any amount of input and output
    print(args)
    print(kwargs)
    
student_info('Math', 'Art', name='John', age=32)
print("\n")
courses=['Math', 'Art']
info={'name': 'John', 'age': 32}

student_info(*courses, **info)
print("\n")
student_info(courses, info)