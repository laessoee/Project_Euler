import math

def digits(n):
    return int(math.log10(fibonacci(n)))+1
    
# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)


def count(x,y,z):
    for i in range(x,y):
        if int(math.log10(fibonacci(i)))+1 == z:
            print("Succes! Fibonacci number:", i, "has", z, "digits")
            break

print(count(4000,5000,1000))


    
    
    

        
        
        