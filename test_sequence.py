# test_sequence.py by mohammed

import sequence 
import mcb185

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGTNRYK'))
print(mcb185.anti_seq('AAAACGTNRYKBDHV')) # this accounts for the ambiguity codes
print(sequence.translate('ATGCCCTAA'))

s = 'ACGTACGTGGGGGACGTACGTCCCCC'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))
