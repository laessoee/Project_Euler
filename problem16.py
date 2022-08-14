

def sumNumber(x,y):
    sum = 0
    digit_string = str(pow(x,y))
    #print(digit_string)
    digit_map = map(int, digit_string)
    #print(digit_map)
    digit_list = list(digit_map)
    #print(digit_list)
    for i in digit_list:
        #print(i)
        sum += i
        
    return sum
    
print(sumNumber(2,1000))