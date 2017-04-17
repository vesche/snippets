rna_trans = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

def to_rna(dna):
    rna = ''
    for n in dna:
        if n not in rna_trans:
            return ''
        rna += rna_trans[n]
    return rna
