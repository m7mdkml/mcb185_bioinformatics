#23hydropathy.py by Mohammed

def kd_hydrophobe(aa):            # The Hydrophobicity scale per aa
    if aa == 'A': return 1.8
    elif aa == 'R': return -4.5
    elif aa == 'N': return -3.5
    elif aa == 'D': return -3.5
    elif aa == 'C': return 2.5
    elif aa == 'Q': return -3.5
    elif aa == 'E': return -3.5
    elif aa == 'G': return -0.4
    elif aa == 'H': return -3.2
    elif aa == 'I': return 4.5
    elif aa == 'L': return 3.8
    elif aa == 'K': return -3.9
    elif aa == 'M': return 1.9
    elif aa == 'F': return 2.8
    elif aa == 'P': return -1.6
    elif aa == 'S': return -0.8
    elif aa == 'T': return -0.7
    elif aa == 'W': return -0.9
    elif aa == 'Y': return -1.3
    elif aa == 'V': return 4.2
    else :
        return ('not an amino acid')

print(kd_hydrophobe('W'))
print(kd_hydrophobe('M'))
print(kd_hydrophobe('X'))
print(kd_hydrophobe('A'))
