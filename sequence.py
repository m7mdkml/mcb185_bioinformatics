# sequence.py by mohammed


# to convert T to U
def transcribe(dna):
    return dna.replace('T', 'U')
    
# makes a library that's reverse and complimentary
def revcomp(dna):
    rc = []
    for nt in dna[::-1]: # [::-1] is what reverses the string
        if   nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else:           rc.append('N')
    return ''.join(rc)
    
# function to translate the start and stop codon
def translate(dna):
    aas = []
    for i in range(0, len(dna), 3): # steps by 3 for codon
        codon = dna[i:i+3]          # creates a codon
        if   codon == 'ATG': aas.append('M')
        elif codon == 'TAA': aas.append('*')
        elif codon == 'TAG': aas.append('*')
        elif codon == 'TGA': aas.append('*')
        else:                aas.append('X')
    return  ''.join(aas)

# same thing without if statements
def translate(dna):
    codons = ('ATG', 'TAA', 'TAG', 'TGA')
    aminos = 'M***'
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon in codons:
            idx = codons.index(codon)
            aa = aminos[idx]
            aas.append(aa)
        else:
            aas.append('X')
    return  ''.join(aas)
    
def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)
    
def gc_skew(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)
    
    
