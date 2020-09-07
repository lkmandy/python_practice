import re
from collections import Counter


class Phrase(object):

    def __init__(self, words):
        self.words = re.sub(r'[^a-z0-9 ]', '', words.lower()).split()
        pass

    def count_words(self):
        return Counter(self.words)

