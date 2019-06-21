import re
from collections import Counter


def count_words(sentence):
    count = {}

    # Allow single quote inside the word only.
    pattern = re.compile(r"([a-z\d]+(?:'[a-z\d]+)?)")

    words = pattern.findall(sentence.lower())

    return dict(Counter(words).most_common())
