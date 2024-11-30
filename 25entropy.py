# 25entropy.py by Mohammed

import math

def shannon_e(a, t, c, g): # calculate Shannon entropy for nucleotide
    total_nt = a + t + c + g
    # needs an if statement for 0 values
    pa = a / total_nt if a > 0 else 0
    pt = t / total_nt if t > 0 else 0
    pc = c / total_nt if c > 0 else 0
    pg = g / total_nt if g > 0 else 0
    
    # negative sign counteracts the positive 
    # needs an if statement for 0 values
    ea = (-pa * math.log2(pa)) if pa > 0 else 0
    et = (-pt * math.log2(pt)) if pt > 0 else 0
    ec = (-pc * math.log2(pc)) if pc > 0 else 0
    eg = (-pg * math.log2(pg)) if pg > 0 else 0
    
    total_e = ea + et + ec + eg
    return total_e

print(shannon_e(25, 25, 25, 25)) # equal entropy, maximum uncertainty
print(shannon_e(25, 25, 25, 0))  # high entropy
print(shannon_e(57, 33, 10, 1))  # high entropy
print(shannon_e(0, 0, 0, 0))     # Nothing
print(shannon_e(1, 2, 3, 94))    # low entropy, G highly likely
print(shannon_e(0, 0, 0, 100))   # only G, no entropy

    
