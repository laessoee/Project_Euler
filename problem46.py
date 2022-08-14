from math import sqrt
from time import sleep

def primeList(x,y): #x must be inequal
# generate prime numbers n EFFICIENT
    primeList = [2]
    for num in range(x,y+1,2):
        if all(num%i!=0 for i in range(3,int(sqrt(num))+1, 2)):
            primeList.append(num)
    return primeList

def oddComposites(x,y): #x must be inequal
    primes = primeList(x,y)
    composites = []
    for num in range(x,y+1):
        if (num not in primes) and (num%2!=0):
            composites.append(num)
    return composites,primes

def goldbachs(x,y):
    composites,primes = oddComposites(x,y)
    goldbachNumbers = []
    for i in composites:
        found = False
        #print("checking", i, "composite")
        #sleep(1)
        for j in primes:
            if (j > i) or found == True:
                break
            #print("checking", j, "prime")
            #sleep(1)
            square = 1
            sum = 2*(square**2) + j
            #print("sum is currently", sum)
            while sum <= i:
                if sum == i:
                    goldbachNumbers.append(i)
                    found = True
                    break
                else:
                    square += 1
                    sum = 2*(square**2) + j
    print(composites)
    print(goldbachNumbers)
    if (composites) == (goldbachNumbers):
        return True
    else:
        return False

print(goldbachs(3,5780))
