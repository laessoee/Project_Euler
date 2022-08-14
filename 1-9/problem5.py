# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:17:25 2020

@author: madsn
"""


def isDivisible(n,k):
    div = True
    for x in range(1,k+1):
        if div == True:
            if n % x == 0:
                div = True
            else:
                div = False
        elif div == False:
            break
    return div

print(isDivisible(3628800,10))
#print(isDivisible(1,3))
p = 3000
# 100.000.000 - 18 ok
# 232792560   - 19 ok
# 232792560   - 20 ok
for x in range(1, p):
    if isDivisible(x, 20) == True:
        print(x)
        break
    
