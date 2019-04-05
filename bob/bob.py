import re
from string import ascii_uppercase, ascii_letters


def hey(phrase):
    if re.search(r'^\s*$', phrase):
        # Empty string, or only whitespace
        return "Fine. Be that way!"

    # Use a set intersection to find all of the chars in the string, both
    # uppercase and lowercase.
    chars = set(ascii_letters).intersection(phrase)

    # Non-empty list of chars, and the uppercase set is a superset of them
    all_uppercase = chars and set(ascii_uppercase).issuperset(chars)

    if all_uppercase and re.search(r'\?\s*$', phrase):
        # All uppercase, followed by '?'
        return "Calm down, I know what I'm doing!"
    elif re.search(r'\?\s*$', phrase):
        # '?' at end
        return "Sure."
    elif all_uppercase:
        # All uppercase
        return "Whoa, chill out!"
    else:
        return "Whatever."
