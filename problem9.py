# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 00:15:26 2020

@author: madsn
"""

def pythagorean(x,y):
    result = 0
    for m in range(2,x):
        for n in range(1,m):
            a = (m**2)-(n**2)
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c == y:
                result = a * b * c
                return (result, a, b, c)
                

print(pythagorean(500,1000))

