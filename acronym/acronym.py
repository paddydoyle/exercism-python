import re


def abbreviate(words):
    # 2nd attempt:
    #
    # Re-do with generator expression, rather than the lambda functools
    # approach. Running lambdas generates a new stack frame.
    # The genexpr does seem a bit nicer.

    return ''.join(x[0] for x in re.split(r'[ \-_]', words) if x).upper()


def abbreviate_functools(words):
    # 1st attempt:
    #
    # Break this down, from inside out:
    # - split into words based on space or '-' (escape '-'!)
    # - filter only non-empty (the '-' could be mid-word, or - between words)
    # - map to extract the first character
    # - join the list into a single string
    # - upper-case the lot
    # All those (())s remind me of LISP!

    return ''.join(map(lambda w: w[0],
                       (filter(None,
                               re.split(r'[ \-]', words))))).upper()
