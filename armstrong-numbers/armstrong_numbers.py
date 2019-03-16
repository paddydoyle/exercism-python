def is_armstrong(n):
    # Convert to string, so we can work on each digit
    n_string = str(n)
    n_len = len(n_string)

    arm_number = sum(map(lambda x: int(x)**n_len, n_string))

    return n == arm_number
