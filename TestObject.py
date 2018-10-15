# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:51:40 2018

@author: Anton
"""

import unittest
import my_class

class TestObject(unittest.TestCase):
    
    def test_add(self):
        result = my_class,my_method()
        self.assertEqual(result, required_result)
        
# run in terminal with python -m unittest TestObject