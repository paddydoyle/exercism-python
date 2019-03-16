def square_of_sum(count):
    """
    Square of the sum of the first N natural numbers.
    """

    sum_of_count = sum(range(count + 1))

    return sum_of_count * sum_of_count


def sum_of_squares(count):
    """
    Sum of the squares of the first N natural numbers.
    """

    return sum(x * x for x in range(count + 1))


def difference(count):
    """
    Difference between the square of the sum, and sum of
    the squares.
    """

    return square_of_sum(count) - sum_of_squares(count)
