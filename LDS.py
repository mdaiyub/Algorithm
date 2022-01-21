# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:39:07 2021

@author: Aiyub
"""

# Python 3 program to find the length of
# the longest decreasing subsequence
 
# Function that returns the length
# of the longest decreasing subsequence
def lds(arr, n):
 
    lds = [0] * n
    max = 0
 
    # Initialize LDS with 1 for all index
    # The minimum LDS starting with any
    # element is always 1
    for i in range(n):
        lds[i] = 1
 
    # Compute LDS from every index
    # in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if (arr[i] < arr[j] and
                lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1
 
    # Select the maximum
    # of all the LDS values
    for i in range(n):
        if (max < lds[i]):
            max = lds[i]
 
    # returns the length of the LDS
    return max
 
# Driver Code
if __name__ == "__main__":
     
    arr = [ 200,300,20,70,210,50,5,20 ]
    n = len(arr)
    print("Length of LDS is", lds(arr, n))
 
# This code is contributed by ita_c