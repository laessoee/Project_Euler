# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:04:12 2020

@author: madsn
"""


def oddEven(n):
    if n % 2 == 0:
        return (n/2)
    else:
        return ((n*3)+1)


# recursive functions sick mr. mads
def chain(n, counter = 1):
    if n == 1:
        return counter
    else:
        return chain(oddEven(n), counter+1)
 
    
# Finds the biggest number with the highest steps, in n numbers
# the function tests 100.000 numbers in 23 seconds. 
# not efficient, but liniar speed.
def biggestChain(n):
    result = 1
    for i in range(1, n+1):
        if i % 100000 == 0:
            print("1x 100k done")
        if chain(result) < chain(i):
            result = i
    return result
            
print(biggestChain(1000000))
