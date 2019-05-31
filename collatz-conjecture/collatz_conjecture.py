def steps(number):
    MAX_ITER = 2**20

    if number < 1:
        raise ValueError("Stictly positive inputs only")

    # Probably overkill to include a max iteration.
    for i in range(MAX_ITER):
        if number == 1:
            break
        elif number % 2 == 0:
            # Even, return n/2
            number = number / 2
        else:
            # Odd, return 3n+1
            number = 3 * number + 1

    if i == MAX_ITER:
        raise ValueError("Hit MAX_ITER. Bailing out!")

    return i
