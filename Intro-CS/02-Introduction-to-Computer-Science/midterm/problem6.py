def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    maxValue = 0
    for i in t:
        if type(i) == tuple or type(i) == list:
            maxValue = max(max_val(i), maxValue)
        elif type(i) == int:
            maxValue = max(i, maxValue)
    return maxValue

print(max_val((5, (1,2), [[1],[9]])))