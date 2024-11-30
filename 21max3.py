# 21max3.py by Mohammed

import math

def max3(a, b, c):      #Function will return the largest input
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: 
        return c

# Examples of us:
print(max3(3, 6, 9)) 
print(max3(3, 6, 6)) 
