# 37nilakantha.py by mohammed

def pi_estimate(n):
    """
Will break up the series in two parts 
to add on each other in the loop
"""
    nila1 = 3 # The first part of the equation is just 3
    sign = 1 # This will be used to turn the value to negative at the end
    
    for i in range(1, n + 1):
        # The second part of the series
        nila2 = 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
        nila1 = nila1 + nila2 * sign # combining the series and adding on
        sign = sign * -1               # switches the sign
        
    return nila1
    
print(pi_estimate(1))
print(pi_estimate(2))
print(pi_estimate(5))
print(pi_estimate(10))
