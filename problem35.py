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
    
def rotate(x):
    #intToList = [int(x) for x in str(x)]
    x.append(x.pop(0))
    return x

def primeList(n):
# generate prime numbers n EFFICIENT
    primeList = [2]
    for num in range(3,n+1,2):
        if all(num%i!=0 for i in range(3,int(sqrt(num))+1, 2)):
            primeList.append(num)
    return primeList
        
def main(x):
    print("initiating primelist...")
    target = primeList(x)
    print("all primes <",x,"listed")
    circularPrimes = []
    for i in target:
        print("computing number",i,end="\r")
        y = intToList(i)
        for j in range(len(y)):
            rotate(y)
            if isPrime(listToInt(y)) == True:
                if (j+1) == len(y):
                    circularPrimes.append(listToInt(y))
                continue
            else:
                break
    print()
    print("finished computing")
    return len(circularPrimes)

num = 1000000
print("number og circular primes \nfor all prime numbers <",num, ": \n>> ", main(num))


