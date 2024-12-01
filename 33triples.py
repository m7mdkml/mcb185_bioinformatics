# 33triples.py by mohammed

import math

def triples(n):
    for a in range(1, n): 
        for b in range(a, n):
            c_square = a**2 + b**2     # Hypotenuse formula
            c = math.sqrt(c_square)    # The square root function returns a float
            if c % 1 == 0:             # makes sure c is a whole number
                print(a, b, c)

print(triples(100))
