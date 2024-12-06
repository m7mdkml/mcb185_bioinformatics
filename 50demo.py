# 50demo.py by mohammed

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print ()

for i in range(len(seq)):
    print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])   # Slices, acts like range()
print(s[0:8:2]) # step sizes, e.g 2
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1]) # last one is inverted

# Tuples, holds multiple values, immutable
tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0]) # 0 to print the first tuple
print(tax[::-1])

def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c)**0.5 / (2*a))
    x2 = (-b - (b**2 - 4 * a * c)**0.5 / (2*a))
    return x1, x2

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)
intercepts = quadratic(5, 6, 1)
print(intercepts[0], intercepts[1])

nts = 'ACTG'
for i in range(len(nts)):
    print(i, nts[i])
# enumerate = range(len( adds 1, 2, 3 before nt
for i, nt in enumerate(nts):
    print(i, nt)

# using zip() 
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
    
# adds nt before names
for nt, name in zip(nt, names):
	print(nt, name)

# zip() and enumerate() can be combined
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)
    
# Lists are tuples but with brackets, mutable
list1 = [1, 2, 3]
list2 = list1
list2[0] = 4
print(list1)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# append to add C in the end
nts.append('C')
print(nts)

# pop to remove and put into another variable
last = nts.pop()
print(last)
print(nts)

# in this case, it sorted alphabetically 
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list() function with no argument creates an empty list
items = list()
print(items)

stuff = []
stuff.append(3)
stuff.append(4)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVW'
print(alph)
aas = list(alph)
print(aas)

"""
split() and join(), will probably be 
used to split and combine sequences
"""
# split by space
text = 'good day        to you'
words = text.split()
print(words)

# split by comma, or whatever
line = '1.41,2.72,3.14'
print(line.split(','))

line = '1.41\t2.72\t3.14'
print(line.split())

# lists into strings using delimiter
s = '-'.join(aas) # this adds '-' in between
print(s)
s = ''.join(aas) # this adds nothing
print(s)

# Searching using in, find() and index()
# in
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

# index()
print('index G?', alph.index('G')) # 6 because 0 is first
# print('index Z?', alph.index('Z')) # error

# find() doesnt work for tuples
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

"""
use in if you are searching through a 
list or tuple and you don't know the element
"""
# if thing in list: idx = list.index(thing)

"""
Files contain data but are not "containers'
they can't be sliced and must be "opened" and "closed"
"""

with open(path) as fp: # fb is a variable, short for "file pointer"
    for line in fp:
        do_something_with(line) # just a stand in
# no need to close the file, its automatically closed when you go beyond "with"  

"""
you  can open compressed files through a python program
instead of uncompressing then opening, the following
structure can be used
"""

# gzip function
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
    print(line, end='')
