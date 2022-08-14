# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:40:27 2020

@author: madsn
"""

from math import sqrt

def isPrime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def getPrime(x):
    count = 0 
    num = 2
    while True:
        if isPrime(num) == True:
            count = count + 1
            if count == x:
                return num
        num = num + 1

print(getPrime(10001))