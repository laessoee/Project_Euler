from math import sqrt

#40755

def triangleSum(x):
    triangle = (x*(x+1))/2
    return triangle
    

def triangle(num):
    sum = -(1/2)+(sqrt(1+8*num))/2
    return sum.is_integer()

def pentagonal(num):
    sum = (1/6)+(sqrt(1+24*num))/6
    return sum.is_integer()

def Hexagonal(num):
    sum = (1/4)+(sqrt(1+8*num))/4
    return sum.is_integer()

def findNum(x):
    count = x
    while True:
        if count % 100000 == 0:
            print("starting calculating", count)
        if (pentagonal(count) == True) and (Hexagonal(count) == True) and (triangle(count) == True):
            return count
        count += 1

#print(findNum(40756))
#1.262.700.000 calculated, not found

def findNumFast(x):
    pass
    count = x
    while True:
        if count % 10000 == 0:
            print("starting calculating triangle number:", count)
        tri = triangleSum(count)
        if (pentagonal(tri) == True) and (Hexagonal(tri) == True):
            return tri
        count += 1
    
#print(findNumFast(40756))
#1.533.776.805