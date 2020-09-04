import re
# check if a word is an isogramm


def is_isogram(word):
    word = re.sub(r"[^a-z]", "", word.lower().replace(' ', ''))
    return len(word) == len(set(word))
