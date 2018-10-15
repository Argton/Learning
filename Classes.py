# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:29:22 2018

@author: Anton
"""

class Person():
    def __init__(self, name):
        self.name=name
        
    def __repr__(self):
        return(self.name)
        
class Student(Person):
    def __init__(self, name, university):
        super(Student, self).__init__(name)
        self.university=university
        
        
    def __repr__(self):
        return(self.name)
        
my_person=Person("Anton")
my_student1=Student(my_person, "Chalmers")
my_student2=Student("Kalle", "Chalmers")

print(my_student1.name)
print(my_student2.name)