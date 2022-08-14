import math

one = ["","one","two","three","four","five","six","seven","eight","nine"]
ten = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
odd = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
hundred = "hundred"
And = "and"
bind = "-"
space = " "

#spell a number
def spell(x):
    if x > 1000:
        return "only works for numbers 1-1000"
    if x == 1000:
        name = "onethousand"
        return name
    if x == 100:
        name = "onehundred"
        return name
    if x == 10:
        name = "ten"
        return name
    hundreds = math.floor(x / 100)
    tenths = math.floor(x / 10) - (hundreds * 10)
    ones = x - (hundreds * 100) - (tenths * 10)
    if x > 99:
        if (x % 100) == 0:
            name = one[hundreds] + hundred
        elif ((tenths * 10) + ones) < 20 and ((tenths * 10) + ones) > 10 :
            name = one[hundreds] + hundred + And + odd[ones]
        else:
            name = one[hundreds] + hundred + And + ten[tenths] + one[ones]
        return name
    if x > 10:
        if ((tenths * 10) + ones) < 20:
            name = odd[ones]
        else:
            name = ten[tenths] + one[ones]
        return name
    else:
        name = one[ones]
        return name

#count letters in a word x
def countLetter(x):
    return len(spell(x))
    
#count letters in number 1 - x
def countWord(x):
    sum = 0
    for i in range(1,x+1):
        sum += len(spell(i))
    return sum
    
#solves euler problem17
print(countWord(1000))
#for i in range(1,1001):
#    print(spell(i))
#print(countWord(5))







