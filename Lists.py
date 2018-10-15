# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:12:28 2018

@author: Anton
"""

courses=["History", "Math", "Physics"]

courses.insert(0, "Art") # can also insert a new list
courses.append("Sports")
morecourses=["Science"]
courses.extend(morecourses)
courses.remove("History")
courses.pop()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
sorted_courses=sorted(courses)
print(sorted_courses)
print(courses.index("Math"))
print("Art" in courses)

for index, course in enumerate(courses):
    print(index, course)
    
course_str = ', '.join(courses)
print(course_str)
new_list=course_str.split(' - ')
print(new_list)

# If list2=list1 and you change an element in list 1 -> you change it in list2 too

# Sets are faster than list and tuples in general. Can only have one of each element in a set,
# and they are not ordered
# some methods: intersection, union, difference

