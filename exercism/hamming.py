def distance(dna_A, dna_B):
    if len(dna_A) != len(dna_B):
        raise ValueError

    hamming = 0
    for i in range(len(dna_A)):
        if dna_A[i] != dna_B[i]:
            hamming += 1
    return hamming
