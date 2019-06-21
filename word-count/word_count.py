import re


def count_words(sentence):
    count = {}

    # Allow single quote inside the word only.
    pattern = re.compile(r"([a-z\d]+(?:'[a-z\d]+)?)")

    words = pattern.findall(sentence.lower())

    for word in words:
        # Is there a better idiom here?
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count
