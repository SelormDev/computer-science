# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here   
    if b == 0:
        return a
    return gcdRecur(b, a%b)
    
print(gcdRecur(1071, 462))
