import re
from collections import Counter


def count_words(sentence):
    # Note: Cound use collections.Counter, but it's slower because of
    # the need to convert it back to a dict() to match the test results.

    count = {}

    # Allow single quote inside the word only.
    pattern = re.compile(r"([a-z\d]+(?:'[a-z\d]+)?)")

    words = pattern.findall(sentence.lower())

    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count
