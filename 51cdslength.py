# 51cdslength by mohammed

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)

import gzip
lengths = []
# never hard code paths
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        lengths.append(end - beg + 1)

# De nesting is preferred 
import gzip
lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                lengths.append(end - beg + 1)
            
