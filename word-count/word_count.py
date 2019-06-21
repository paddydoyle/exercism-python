import re
from collections import Counter


def count_words(sentence):
    return Counter(sentence).most_common()
