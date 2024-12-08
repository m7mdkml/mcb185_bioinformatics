import math
# function that returns minimum value, instead of min()

def minimum(values):
    mini = values[0]
    for i in values[1:]:
            if i < mini: mini = val  
    return mini
    
# same function but it returns min and max

def minmax(values):
    mini = values[0]
    maxi = values[0]
    for i in values:
        if i < mini: mini = i
        if i > maxi: maxi = val
    return mini, maxi
    
# mean()

def mean(values):
    total = 0
    for i in values: total += i
    return total / len(values)
    
# entropy

def entropy(probs):
    h = 0
    for p in probs:
        h -= p * math.log2(p)
    return h
print(entropy([0.2, 0.3, 0.5]))

# dkl()

def dkl(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += p * math.log2(p/q)
    return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))
