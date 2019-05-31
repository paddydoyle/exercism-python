def steps(number):
    if number < 1:
        raise ValueError("Stictly positive inputs only")

    count = 0

    # Assuming the conjecture is true, so no additional
    # guard condition!
    while number != 1:
        if number % 2 == 0:
            # Even, return n/2
            number = number / 2
        else:
            # Odd, return 3n+1
            number = 3 * number + 1

        count += 1

    return count
