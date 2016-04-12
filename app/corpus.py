from collections import defaultdict
from statistics import median


class Corpus(object):
    def __init__(self):
        self._alphagram_to_words = defaultdict(lambda: set())

    def add_words(self, words):
        for word in words:
            alphagram = self._get_alphagram(word)
            self._alphagram_to_words[alphagram].add(word)

    def get_anagrams(self, word, limit=None):
        alphagram = self._get_alphagram(word)
        anagrams = self._alphagram_to_words[alphagram]
        if word not in anagrams:
            return []
        anagrams_without_query_word = [anagram for anagram in self._alphagram_to_words[alphagram] if anagram != word]
        return anagrams_without_query_word[:limit]

    def remove_word(self, word):
        alphagram = self._get_alphagram(word)
        self._alphagram_to_words[alphagram].discard(word)

    def clear(self):
        self._alphagram_to_words.clear()

    def get_stats(self):
        word_lengths = []
        for _, words in self._alphagram_to_words.items():
            word_lengths += [len(word) for word in words]
        stats = {'count': len(word_lengths),
                 'min_length': min(word_lengths),
                 'max_length': max(word_lengths),
                 'med_length': median(word_lengths),
                 'ave_length': sum(word_lengths)/len(word_lengths)}
        return stats

    @classmethod
    def _get_alphagram(cls, word):
        return ''.join(sorted(word))
