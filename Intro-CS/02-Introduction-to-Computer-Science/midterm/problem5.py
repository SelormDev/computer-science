# Paste your function here
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    invertedDic = {}
    for key in d:
        if d[key] in invertedDic:
            invertedDic[d[key]].append(key)
            invertedDic[d[key]].sort()
        else:
            invertedDic[d[key]] = [key]
    return invertedDic
        
d = {4:True, 2:True, 0:True}
print(dict_invert(d))