def intToList(x):
    return [int(x) for x in str(x)]

def listToInt(x):
    res = sum(d * 10**i for i, d in enumerate(x[::-1]))
    return res

def intToBinary(x):
    return ("{0:0b}".format(x)) #return binary in string format

def reverseString(x):
    return x[::-1]

def palindricIntegers(x):
    masterList = []
    for i in range(1,(x+1)):
        if str(i) == reverseString(str(i)):
            masterList.append(i)
    return masterList

def main(x):
    print("initiating palindrome list")
    target = palindricIntegers(x)
    print(f"palindromes <{x} computed")
    masterList = []
    for i in target:
        print("testing palindrom", i, " >>> ",intToBinary(i), end="\r")
        if intToBinary(i) == reverseString(intToBinary(i)):
            masterList.append(i)
    print()
    return sum(masterList)

print(main(1000000))
            



