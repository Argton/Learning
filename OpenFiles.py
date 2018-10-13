# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:18:21 2018

@author: Anton
"""

# Opening textfile in different ways

f=open('test.txt','r')
print("f.read(), everything: ")
print(f.read())
f.close()

print("\n")
with open('test.txt','r') as g: #context manager. needs no close statement
    print("g.readLines(): ")
    print(g.readlines())        
     
print("\n")    
with open('test.txt','r') as g:
    print("g.read 20 first characters in the file: ")
    print(g.read(20))     

print("\n")
with open('test.txt','r') as g: 
    print("g.readLine(5), 5 first characters in first line: ")
    print(g.readline(5))         

print("\n")    
with open('test.txt','r') as g:
    print("g.read, everything: ") 
    print(g.read()) # reads everything
      
    
print("\n")    
print("Check if closed: ")
print(g.closed)

# Opening picture

with open('pic.jpg','rb') as rf:    
    with open('pic.jpg','wb') as wf:    
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    
