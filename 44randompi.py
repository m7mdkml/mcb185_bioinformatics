# 44randompi.py by mohammed

import random
import math

# pi estimate using the Monte Carlo method
inside = 0 # Will go up each time the dart is in the circle
total = 0 # Total throws

while True:
    x = random.random()
    y = random.random()

    distance = math.sqrt(x**2 + y**2)
    
    if distance < 1:
        inside += 1
    total +=1
    pi = 4 * (inside / total)
    print(pi)
