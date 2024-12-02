# 42chicago.py by mohammed

import random

games = 1000000
log = games // 100
total = 0
zeroes = 0
for i in range(games):
    if 1 % log == 0: print(f'{100 * i/games:.0f}')
    score = 0
    for target in range(2, 13): # has to be 13 to get to 11
        if random.randint(1, 6) + random.randint(1, 6) == target:
            score += target
        if score == 0: zeroes += 1
        total += score
        
print(total / games)
print(zeroes / games)
