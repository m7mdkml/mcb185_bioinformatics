# 26phred.py by mohammed

import math

def convert(x):
# function will trigger different equation depending on input
    
    if 0 < x < 1:
    # Probability to PHRED conversion
        return -10 * math.log10(x)
    elif x > 1:
    # PHRED to probability conversion
        return 10**(-x / 10)   
    else:
        return 'values of 0 and 1 are not permitted'
        
print(convert(20))
print(convert(0.01))
print(convert(0))
print(convert(1))
