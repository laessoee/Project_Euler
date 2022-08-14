

def calculateBigAssNumber(x):
    sum = 0
    for i in range(1,(x+1)):
        sum += i**i
    print(sum)

calculateBigAssNumber(1000)



