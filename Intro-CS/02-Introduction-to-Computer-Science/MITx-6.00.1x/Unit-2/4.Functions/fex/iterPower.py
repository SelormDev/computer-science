def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    ans = base
    if exp == 0:
            return 1.000
    
    while (exp > 1):
        ans = ans * base
        exp = exp - 1

    return ans
    
print(iterPower(2, 0))