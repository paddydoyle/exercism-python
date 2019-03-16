import re


def verify(isbn):
    # Basic validation
    if not isbn:
        return False

    # Proper structure validation
    if not re.match(r'^\d\-?\d{3}\-?\d{5}\-?[0-9X]$', isbn):
        return False

    # Remove any '-'s
    isbn = isbn.replace('-', '')

    # Split off the last character, which may be an 'X'
    isbn_prefix = isbn[0:-1]
    isbn_suffix = isbn[-1]

    checksum_total = 0

    # First process the first 9 characters
    # Double-loop-counters:
    # - first is the char
    # - second is from the range 10,9,8...,2
    for i, r in zip(isbn_prefix, range(10, 1, -1)):
        checksum_total += (int(i) * r)

    # Then add the final character
    if isbn_suffix == 'X':
        checksum_total += 10
    else:
        checksum_total += int(isbn_suffix)

    # Checksum for the result
    return checksum_total % 11 == 0
