def is_leap_year(year):
    # Exclude most years: non-divisible by 4
    if year % 4 != 0:
        return False

    # It is divisible by 4.
    # Next test: is it divisible by 100, but not by 400?
    if year % 100 == 0 and year % 400 != 0:
        return False

    # Otherwise, it is indeed a leap year.
    return True
