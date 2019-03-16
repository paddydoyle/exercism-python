def is_pangram(sentence):
    """
    Test to see if the 'sentence' contains all ASCII characters
    from 'a' to 'z'. Case insensitive.
    Assume true, and look for counter-example.
    """

    # FIXME: can we use a range to define this?
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # FIXME: is this a good idea if the input is huge?
    sentence = sentence.lower()

    # Assume true.
    # Loop over every letter in the alphabet, looking for counter-examples.
    for letter in alphabet:
        if letter not in sentence:
            return False

    # No counter-examples found, so must be true.
    return True


def is_pangram2(sentence):
    """
    Trying out more core Python features like map and filter.
    """

    # Lower-case ascii
    alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

    # For each letter, test if neither lower nor upper case version
    # is in the sentence. If so, we've found counter-examples.
    missing_letters = list(filter(lambda letter: letter not in sentence and
                                  letter.upper() not in sentence, alphabet))

    return len(missing_letters) == 0
