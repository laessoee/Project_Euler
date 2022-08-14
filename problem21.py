#just a optimal function of cointing divisors
def divisors(n):
    count = 1  # accounts for '1'
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    return count

#bruteforce list of divisors    
def listBruteforce(n):
    divisors = []
    for i in range(1, int(n/2+1)):
        if n%i == 0:
            divisors.append(i)
    return divisors

#Sum of list
def sumDiv(n):
    return sum(listBruteforce(n))

#check if n is amiceable        
def isAmicable(n):
    if (n == sumDiv(sumDiv(n)) and n != sumDiv(n)):
        return True
    else:
        return False

#summing all amiceable < n
def sumAmicable(n):
    Sum = 0
    for i in range(1,n):
        if isAmicable(i) == True:
            Sum = Sum + i
    return Sum   
    
print(sumAmicable(10000))
