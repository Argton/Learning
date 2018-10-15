# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:04:07 2018

@author: Anton
"""

import csv

with open('textfile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) 
    
    for line in csv_reader:
        print(line)
        
 # csv.writer(new_file, delimiter='-') # delimiter='\t'
 # csv_writer.writerow(line)
 # csv_reader = csv.DictReader(csv_file) 
 # csv_writer = csv.DictWriter(csv_file) 
 # del line['email']
 # csv_writer.writeheader() 