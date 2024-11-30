# 22oligotemp.py by Mohammed

import math

def oligo(a, t, c, g):
"""
input the number of As, Ts, Cs and Gs in the oligo
in the following function to calculate tm 
"""
    nt = a + t + c + g
    if nt <= 13: 
        tm = (a + t)*2 + (g + c)*4  # for short oligos
    else:                           
        tm = 64.9 + 41 * (g + c - 16.4)/ nt  # for long oligos
        
    return tm

print(oligo(2, 3, 2 ,1))
print(oligo(8, 8, 6 ,6))
