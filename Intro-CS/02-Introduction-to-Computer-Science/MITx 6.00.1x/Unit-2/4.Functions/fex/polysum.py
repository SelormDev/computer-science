from math import *

def polysum(n, s):
    return round(((0.25*n*s**2)/tan(pi/n)) + ((s * n)**2), 4)