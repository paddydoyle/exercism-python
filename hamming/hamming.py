def distance(strand_a, strand_b):
    # First check the lengths
    if len(strand_a) != len(strand_b):
        raise ValueError('Hamming distance undefined for unequal sequence ' +
                         'lengths')

    distance = 0

    # zip() returns an iterator of tuples, stopping at the shortest.
    for a, b in zip(strand_a, strand_b):
        if a != b:
            distance += 1

    return distance
