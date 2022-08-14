from math import sqrt


def isPrime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def intToList(x):
    return [int(x) for x in str(x)]

def listToInt(x):
    res = sum(d * 10**i for i, d in enumerate(x[::-1]))
    return res

def truncatateLeft(x):
    y = intToList(x)
    y.pop(0)
    return listToInt(y)

def truncatateRight(x):
    y = intToList(x)
    y.pop()
    return listToInt(y)

def primeList(x,y): #x must be inequal
# generate prime numbers n EFFICIENT
    primeList = []
    for num in range(x,y+1,2):
        if all(num%i!=0 for i in range(3,int(sqrt(num))+1, 2)):
            primeList.append(num)
    return primeList


def run(rangeMin, rangeMax):
    target = primeList(rangeMin, rangeMax)
    #print(target) #----------
    specialPrimes = []
    for i in target:
        #print("scanning", i) #-----------
        subTarget = intToList(i)
        length = len(subTarget)
        subTargetLeft = i
        subTargetRight = i
        res = True
        for j in range(1, length):
            subTargetLeft = truncatateLeft(subTargetLeft)
            #print("scanning branch", subTargetLeft) #-------------
            if isPrime(subTargetLeft) == True:
                #print(subTargetLeft, "is prime") #-------------
                continue
            else:
                #print(subTargetLeft, "is not") #---------------
                res = False
                break
        for l in range(1, length):
            subTargetRight = truncatateRight(subTargetRight)
            #print("scanning branch", subTargetRight) #---------------
            if isPrime(subTargetRight) == True:
                #print(subTargetRight, "is prime") #-------------
                continue
            else:
                #print(subTargetRight, "is not") #---------------
                res = False
                break
        if res == True:
            specialPrimes.append(i)
    return specialPrimes

print(sum(run(11,1000000)))



