#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:30:02 2022

@author: allservices
"""

class Rectangle:
   # Defining attributes required for the class
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   # Functionality for the class
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
   
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000

# objects getting initiated with class (arguments should be the )
object1 = Rectangle(160, 120, 2000)
object2 = Rectangle(10, 120, 2000)


method1 = object1.calculate_cost()

print("Area of Rectangle object1 : %s sq units" % (object1.get_area()))
print("Area of Rectangle object2 : %s sq units" % (object2.get_area()))

print("Area Cost object1 : %s Euros" % (method1))
 

''' SAMPLE OUTPUT
Area of Rectangle object1 : 19200 sq units
Area of Rectangle object2 : 1200 sq units
Area Cost Object1: 38400000 Euros
'''
