from collections import defaultdict


class Corpus(object):
    def __init__(self):
        self._alphagram_to_words = defaultdict(lambda: set())

    def add_words(self, words):
        for word in words:
            alphagram = self._get_alphagram(word)
            self._alphagram_to_words[alphagram].add(word)

    def get_anagrams(self, word, limit=None):
        alphagram = self._get_alphagram(word)
        anagrams = [anagram for anagram in self._alphagram_to_words[alphagram] if anagram != word]
        return anagrams if limit is None else anagrams[:limit]

    def remove_word(self, word):
        alphagram = self._get_alphagram(word)
        self._alphagram_to_words[alphagram].discard(word)

    def clear(self):
        self._alphagram_to_words.clear()

    @classmethod
    def _get_alphagram(cls, word):
        return ''.join(sorted(word))
