# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:11:59 2021

@author: Aiyub
"""

def CircleArea(r):
    PI = 3.14
    return PI * (r*r)

r = int(input("Enter The Redious: "))
print("Area of circle = %.3f" % CircleArea(r))


    