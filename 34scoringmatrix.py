# 34scoringmatrix.py by Mohammed

alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

# first indent 
print(' ', end=' ')

for nt in alphabet:
    print(nt, end=' ')
print ()

for x_nt in alphabet:
    print(x_nt, end=' ') 

    for y_nt in alphabet:
        if x_nt == y_nt:
            print(match, end=' ')
        else:
            print(mismatch, end=' ')
    print()

"""
Output is similar enough
"""
