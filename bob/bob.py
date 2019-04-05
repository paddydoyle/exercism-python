def hey(phrase):
    phrase = phrase.strip()

    if not phrase:
        # Empty string, or only whitespace
        return "Fine. Be that way!"

    if phrase.isupper() and phrase.endswith('?'):
        # All uppercase, followed by '?'
        return "Calm down, I know what I'm doing!"
    elif phrase.isupper():
        # All uppercase
        return "Whoa, chill out!"
    elif phrase.endswith('?'):
        # '?' at end
        return "Sure."
    else:
        return "Whatever."
