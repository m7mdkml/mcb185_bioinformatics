# 41zscores.py by mohammed

import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000

for i range(limit):
    r = random.gauss(0.0, 1.0) # mean and s.deviation are floats
    if r > 1: z1 = z1 + 1
    if r > 2: z2 = z2 + 1
    if r > 3: z3 = z3 + 1

print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)
