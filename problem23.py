
    
    
#bruteforce list of divisors
def listBruteforce(n):
    divisors = []
    for i in range(1, int(n/2+1)):
        if n%i == 0:
            divisors.append(i)
    return divisors
    
#return True for abundant number, else false
def isAbundant(n):
    divisors = listBruteforce(n)
    holder = 0
    for i in divisors:
        holder = holder + i
    if holder > n:
        return True
    else:
        return False
    

#abundantNumbers = []
#nonAbundant = []
#for i in range(1,30001):
#    if i % 1000 == 0:
#        print(i,"is done")
#    if isAbundant(i) == True:
#        abundantNumbers.append(i)
#    else:
#        nonAbundant.append(i)
        
import json 
import pickle


small = [1,2,3,4,5]
#with open('problem23.txt','w') as filehandle:
#    json.dump(small,filehandle)
with open('problem23.data','wb') as filehandle:
    pickle.dump(small,filehandle)
small2 = []
with open('problem23.data','rb') as filehandle:
    small2 = pickle.load(filehandle)
print(small2)
