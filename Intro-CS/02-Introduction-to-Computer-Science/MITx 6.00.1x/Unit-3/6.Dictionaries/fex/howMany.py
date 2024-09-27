animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    totalAnimals = 0
    for animals in aDict:
        totalAnimals += len(aDict[animals])
    
    return totalAnimals

print(how_many(animals))