# 40cdslength.py by mohammed

import gzip
import sys


# this will report the lengths of protien coding genes in E. coli genome
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#': # skips comments
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1)
                
# using continue statements results in an easier to read code
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)
                
                
