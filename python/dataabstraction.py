#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:48:27 2022

@author: allservices
"""


class MyClass:
  
    # Hidden member of MyClass
    __hiddenVariable = 0
    
    # A member method that changes 
    # __hiddenVariable 
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)
   
# Driver code
myObject = MyClass()     
myObject.add(2)
myObject.add(5)
  
# This line causes error
print (myObject.__hiddenVariable)

''' SAMPLE OUTPUT
2
7
Traceback (most recent call last):
  File "filename.py", line 13, in 
    print (myObject.__hiddenVariable)
AttributeError: MyClass instance has 
no attribute '__hiddenVariable' 
'''
