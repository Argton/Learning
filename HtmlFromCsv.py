# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:11:03 2018

@author: Anton
"""

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv.data = csv.reader(data_file)

    # skip header and first line    
    next(csv_data)
    next(csv_data)
    
    for line in csv_data:
        names.append(f"{line[0]}{line[1]}")
        
html_output += f"<p>There are currently {len(names) public contributors. Thank you!</p>}"

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<li>{name}</li>"
    
html_output += "\n</ul>"

print(html_output)