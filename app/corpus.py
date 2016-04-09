from collections import defaultdict


class Corpus(object):
    def __init__(self):
        self._alphagram_to_words = defaultdict(lambda: [])

    def add_words(self, words):
        for word in words:
            alphagram = self._get_alphagram(word)
            self._alphagram_to_words[alphagram].append(word)

    def get_anagrams(self, word):
        alphagram = self._get_alphagram(word)
        anagrams = [anagram for anagram in self._alphagram_to_words[alphagram] if anagram != word]
        return anagrams

    def remove_word(self, word):
        alphagram = self._get_alphagram(word)
        self._alphagram_to_words[alphagram].remove(word)

    def clear(self):
        self._alphagram_to_words = defaultdict(lambda: [])

    @classmethod
    def _get_alphagram(cls, word):
        return ''.join(sorted(word))
