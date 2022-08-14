

def distinctPowers(n, minimum, maximum):
    distinctPowersList = []
    for i in range(minimum, (maximum + 1)):
        x = n**i
        if x not in distinctPowersList:
            distinctPowersList.append(x)
    return distinctPowersList

def compareMergeList(mainList, subList):
    for elmnt in subList:
        if elmnt not in mainList:
            mainList.append(elmnt)
    return mainList

def main(rangeMin, rangeMax):
    masterList = []
    for i in range(rangeMin, (rangeMax + 1 )):
        compareMergeList(masterList, distinctPowers(i,rangeMin,rangeMax))
        print("computed", i, end='\r')

    print()
    return len(masterList)
    
#print(compareMergeList(masterList, distinctPowers(2,2,5)))
#print(compareMergeList(masterList, distinctPowers(3,2,5)))
#print(compareMergeList(masterList, distinctPowers(4,2,5)))

print(main(2,100))
