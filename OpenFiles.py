# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:18:21 2018

@author: Anton
"""


f=open('test.txt','r') # r+, w
print("f.read(), everything: ")
print(f.read())
f.close() # always have to close if not using context manager

print("\n")
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.readLines(): ")
    print(g.readlines())        
     
print("\n")    
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.read 20 first characters in the file: ")
    print(g.read(20))     

print("\n")
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.readLine(5), 5 first characters in first line: ")
    print(g.readline(5))         

g.seek(0) # change position to start of file

print("\n")    
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.read, everything: ") 
    print(g.read()) # reads everything
      
print("\n")    
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.read, everything: ") 
    print(g.read(), end="*") # reads everything, puts * at the end
    print("\n")
    print(g.tell()) # how many characters read in
    
print("\n")    
print("Check if closed: ")
print(g.closed)


with open('pic.jpg','rb') as rf:    
    with open('pic.jpg','wb') as wf:    
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    
