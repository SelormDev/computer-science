animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'dog', 'dingo'], 'd': ['donkey']}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    values = aDict.values()
    maxValue = 0
    for value in values:
        print(value)
        if len(value) > maxValue:
            maxValue = len(value)
    
    for key in aDict:
        if len(aDict[key]) == maxValue:
            return key
    

print(biggest(animals))
