# 20demo.py by Mohammed_Al-Kubati

import math

a = 3                           # Just testing 
b = 4                           # the Pythagoras theorem
c = math.sqrt(a**2 +b**2)       # to find hypotenuse
print (c)

print(type(a), type(b), type(c), sep=',') # testing types

def pythagoras(a, b):               #Pythagoras functions
    return math.sqrt(a**2 + b**2)
    
print(pythagoras(2,2))

def invert(nm):  # Inverts the sign of any given number
    return -nm

print(invert(-3))
print(invert(4))

def circum(r):              #function for circumference
    return (2*math.pi*r)

print (circum(3))

s = 'hello'
print(s, type(s))

def is_even(x):
    if x % 2 == 0: return True
    return False
    
print(is_even(2))
print(is_even(3))

c = 45 == b
print(c)
print(type(c))

if a < b:          #Just testing boolean
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')

def comp_dna(bp):
    if bp == 'A':
        return 'T'
    elif bp == 'T':
        return 'A'
    elif bp == 'C':
        return 'G'
    elif bp == 'G':
        return 'C'
        
print (comp_dna('G'))

