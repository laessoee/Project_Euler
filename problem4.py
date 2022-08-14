# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:38:35 2020

@author: madsn
"""
"""
#inverd list
list1 = [1,2,3]
list1.reverse()
print(list1)
"""

""" 
#convert number to list of integers
a = 123
print(a)
b = str(a)
print(b)
c = map(int, b)
print(c)
d = list(c)
print(d)
"""



def biggest(k,q):
    d = 0
    for x in range(1,k):
        for y in range(1,q):
            a = x * y
            b = list(map(int, str(a))) 
            c = list(map(int, str(a)))
            b.reverse()
            if b == c:
                if a > d:
                    d = a
    return d

print(biggest(1000,1000))

          