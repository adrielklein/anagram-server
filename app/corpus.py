from collections import defaultdict
from statistics import median


class Corpus(object):
    def __init__(self):
        self._alphagram_to_words = defaultdict(lambda: set())

    def add_words(self, words):
        for word in words:
            alphagram = self._get_alphagram(word)
            self._alphagram_to_words[alphagram].add(word)

    def get_anagrams(self, query_word, limit=None):
        alphagram = self._get_alphagram(query_word)
        words_for_alphagram = self._alphagram_to_words[alphagram]
        if query_word not in words_for_alphagram:
            return []
        anagrams = [word for word in words_for_alphagram if word != query_word]
        return anagrams[:limit]

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
                 'min_length': min(word_lengths) if word_lengths else 0,
                 'max_length': max(word_lengths) if word_lengths else 0,
                 'med_length': median(word_lengths) if word_lengths else 0,
                 'ave_length': sum(word_lengths) / len(word_lengths) if word_lengths else 0}
        return stats

    def get_most_anagrams(self):
        if len(self._alphagram_to_words) == 0:
            return {}
        num_words_to_alphagram = defaultdict(lambda: [])
        max_num_anagrams = self._get_max_num_anagrams(num_words_to_alphagram)
        alphagrams_with_most_anagrams = num_words_to_alphagram[max_num_anagrams]
        return {alphagram: list(self._alphagram_to_words[alphagram]) for alphagram in alphagrams_with_most_anagrams}

    def _get_max_num_anagrams(self, num_words_to_alphagram):
        for alphagram, words in self._alphagram_to_words.items():
            num_words_to_alphagram[len(words)].append(alphagram)
        max_num_anagrams = max(num_words_to_alphagram.keys())
        return max_num_anagrams

    @classmethod
    def _get_alphagram(cls, word):
        return ''.join(sorted(word))
