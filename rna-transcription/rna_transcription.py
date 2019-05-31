def to_rna(dna_strand):
    mappings = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
            }

    return ''.join(mappings[d] for d in dna_strand)
