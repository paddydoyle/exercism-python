def sum_of_multiples(limit, factors):
    multiples = set()

    for factor in factors:
        # Special case: if factor is 0
        if not factor:
            continue

        # All multiples of factor
        i = factor
        while i < limit:
            # But only keep unique multiples, over all values in factor list.
            multiples.add(i)
            i += factor

    return sum(multiples)
