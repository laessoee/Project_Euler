# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:36:19 2020

@author: madsn
"""
from math import sqrt

primeList = [2]
n = 2000000

# generate prime numbers n EFFICIENT

for num in range(3,n+1,2):
    if all(num%i!=0 for i in range(3,int(sqrt(num))+1, 2)):
        primeList.append(num)
        
print(sum(primeList))