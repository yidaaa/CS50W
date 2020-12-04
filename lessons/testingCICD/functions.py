import math

def square(x):
    return x * x

# write multiple statements to test function
# if assert is true, returns nothing, else error
assert square(10) == 100

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True 
