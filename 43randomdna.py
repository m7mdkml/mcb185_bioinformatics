# 43randomdna.py by mohammed

import random

def seq_number(n): 
    for i in range(1, n+1):
        print (f'>seq-{i}') # prints header
        seq_length = random.randint(40, 70) # random length between two values
        for p in range(seq_length):
            print(random.choice('ATCG'), end='')
        print()

print(seq_number(4))
    
