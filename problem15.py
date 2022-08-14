# Problem15


def factorial(x, result=1):
    if x == 1:
        return result
    else:
        return factorial(x-1, result = result * x)

def grid(x,y):
    totalmoves = x + y
    numerator = factorial(totalmoves)
    denominator = factorial(x) * factorial(totalmoves - x)
    return(numerator / denominator)

print(grid(10,10))
