#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:59:17 2022

@author: allservices
"""

class Bird:
   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class sparrow(Bird):
   
    def flight(self):
        print("Sparrows can fly.")
 
class ostrich(Bird):
 
    def flight(self):
        print("Ostriches cannot fly.")

# Parent class bird inherited to sparraw class and ostrich class
# flight functon from the Bird class has different form in sparrow class and ostrich class


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()

# Relatime Example for Polymorphism
# a person who at the same time can have different characteristics. i.e 
# same time is a father, a husband, and an employee. So the same person exhibits different behavior in different situations.

''' SAMPLE OUTPUT
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
'''
