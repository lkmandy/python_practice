import re
# check if a word is an isogramm


def is_isogram(word):
    word = re.sub(r"[^a-z]", "", word.lower().strip())
    return len(word) == len(set(word))
