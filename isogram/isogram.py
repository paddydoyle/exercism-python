def is_isogram(string):
    # Extract only alphabetic chars, as lower case.
    all_chars = [ch.lower() for ch in string if ch.isalpha()]

    # No duplicates in a set, so test for equal lengths.
    return len(all_chars) == len(set(all_chars))
