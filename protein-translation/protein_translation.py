from itertools import takewhile


def proteins(strand):
    # Map the codon to their protein
    codon_mappings = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan'
    }

    # Put the stop words into a set, since they don't map to
    # anything. Not sure if this is better than just putting them
    # into the dict above.
    codon_stop = set()
    codon_stop.add('UAA')
    codon_stop.add('UAG')
    codon_stop.add('UGA')

    # Split the strand into codons
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    # Return a list
    proteins = []

    # Stop the search using takewhile
    return [codon_mappings[codon] for codon in
            takewhile(lambda c: c not in codon_stop, codons)]
