def sum_of_multiples(limit, factors):
    multiples = set()

    for factor in factors:
        # Special case: if factor is 0
        if not factor:
            continue

        # Add the list of multiples of factor to the set
        multiples.update(range(factor, limit, factor))

    return sum(multiples)
