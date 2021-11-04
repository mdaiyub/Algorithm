# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:50:39 2021

@author: Aiyub
"""

def Minimum_Val(arr):

    return (min(arr))

def Maximum_Val(arr):

    return (max(arr))

arr = list(map(int, input("Enter The elements of an array: ").split()))
Found1 = Minimum_Val(arr)
Found2 = Maximum_Val(arr)

print ("Largest in given array is",Found1)
print ("Smallest in given array is",Found2)

