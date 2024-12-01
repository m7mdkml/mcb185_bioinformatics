# 36poisson.py by mohammed

import math

def poisson(n, k):
    # formula for poisson probability
    probability = ( n**k * math.e**-n) / math.factorial(k) 
    
    return probability
    
print(poisson(5, 10))
print(poisson(0, 2))
