import re
from collections import Counter


def count_words(sentence):
    RE_WORD_INCL_SINGLE_QUOTE = r"([a-z\d]+(?:'[a-z\d]+)?)"

    # Allow single quote inside the word only.
    pattern = re.compile(RE_WORD_INCL_SINGLE_QUOTE)

    return Counter(match.group()
                   for match in pattern.finditer(sentence.lower()))
