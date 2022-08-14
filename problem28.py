

'''

 73 74 75 76 77 78 79 80 81
 72 43 44 45 46 47 48 49 50
 71 42 21 22 23 24 25 26 51
 70 41 20 07 08 09 10 27 52
 69 40 19 06 01 02 11 28 53
 68 39 18 05 04 03 12 29 54
 67 38 17 16 15 14 13 30 55
 66 37 36 35 34 33 32 31 56
 65 64 63 62 61 60 59 58 57
 
 3x3 = 25 = 1 + 3 + 5 + 7 + 9
 5x5 = 101 = 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25
 7x7 = 261 = 101 + 31 + 37 + 43 + 49
 9x9 = 537 = 261 + 57 + 65 + 73 + 81
'''
def sum(x):
    matrix = 1
    sumMatrix = 1
    counting = True
    valueSkip = 1
    valueStep = 1
    if x % 2 == 0:
        return "FALSE, input must be unequal number"
    if x == 1:
        return 1
    while counting == True:
        matrix += 2
        valueStep = valueStep + 1 + valueSkip
        sumMatrix += valueStep
        valueStep = valueStep + 1 + valueSkip
        sumMatrix += valueStep
        valueStep = valueStep + 1 + valueSkip
        sumMatrix += valueStep
        valueStep = valueStep + 1 + valueSkip
        sumMatrix += valueStep
        
        valueSkip += 2
        #print("matrix:", matrix, "x", matrix, "is calculated")
        if matrix == x:
            counting = False
    
    return sumMatrix
        
        
    
print(sum(1001))