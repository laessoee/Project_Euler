# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:19:46 2020

@author: madsn
"""

import math

def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)

n = 1000000
triList = []

holder = 0

for i in range(1, n+1):
    holder = holder + i
    triList.append(holder)

print(max(triList))

def divisibles(x,y):
    for i in x:
        if get_factors(i) > y:
            return i
        
print(divisibles(triList,500))
                
            
