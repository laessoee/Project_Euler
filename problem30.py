import math
import numpy as np
import ast

file1 = open("problem30.txt", "r") #open txt file to write
file2 = file1.read() #download txt file to variable file2
file1.close()

file3 = []
if len(file2) == 0:
    file3 = []
else:
    file3 = ast.literal_eval(file2)

correctNumbers = file3
Lenght = 0

if len(file3) == 0:
    Lenght = 0
else:
    Lenght = len(file3) - 1
    
print("lenght", Lenght)    

file1 = open("problem30.txt", "w") #open txt file to write 


def fifthSum(x):
    list = [int(x) for x in str(x)]
    sum = 0
    for i in list:
        sum += (i**5)
    return sum
    
def factorials(x):
    list = [int(x) for x in str(x)]
    sum = 0
    for i in list:
        sum += (math.factorial(i))
    return sum
    
def auto():
    if correctNumbers == []:
        print("initial list:", correctNumbers)
        print("first run")
        for i in range(2, 1000000):
            if factorials(i) == i:
                print("found correct number:", i)
                correctNumbers.append(i)

        
    else:    
        print("initial list:", correctNumbers)
        print("starting from:", file3[Lenght])
        for i in range((file3[(Lenght)] + 1), (file3[(Lenght)] + 10000000)):
            if factorials(i) == i:
                print("found correct number:", i)
                correctNumbers.append(i)

    return 0

auto()
file1.write(str(correctNumbers))
file1.close()
