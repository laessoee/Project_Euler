# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:58:27 2020

@author: madsn
"""


primeList = []
n = 10000

# generate prime numbers n INEFFICIENT
for allPrimes in range(2, n+1):
    prime = True
    for x in range(2, allPrimes):
        if allPrimes % x == 0:
            prime = False
    if prime == True:
        primeList.append(allPrimes)    
        
# print(primeList)

# find biggest prime factor
def biggestFactor(a):
    b = 0
    for x in primeList:
        if a % x == 0:
            if x > b:
                b = x
    return b

print(biggestFactor(600851475143))
