def test_when_stats_method_is_called_with_empty_corpus_then_return_empty_stats(corpus):
    stats = corpus.get_stats()
    assert 5 == len(stats)
    assert 0 == stats['count']
    assert 0 == stats['min_length']
    assert 0 == stats['max_length']
    assert 0 == stats['med_length']
    assert 0 == stats['ave_length']


def test_when_stats_method_is_called_with_populated_corpus_then_return_stats(corpus):
    corpus.add_words(['it', 'dog', 'person'])
    stats = corpus.get_stats()
    assert 5 == len(stats)
    assert 3 == stats['count']
    assert 2 == stats['min_length']
    assert 6 == stats['max_length']
    assert 3 == stats['med_length']
    assert 11 / 3 == stats['ave_length']


def test_when_most_anagrams_method_is_called_with_empty_corpus_then_return_empty_hash_table(corpus):
    alphagram_to_words = corpus.get_most_anagrams()
    assert 0 == len(alphagram_to_words)


def test_when_most_anagrams_method_is_called_with_populated_corpus_then_return_words_with_most_anagrams(corpus):
    corpus.add_words(['read', 'dare'])
    corpus.add_words(['brag', 'grab'])
    corpus.add_words(['it'])
    alphagram_to_words = corpus.get_most_anagrams()
    assert 2 == len(alphagram_to_words)
    assert ['dare', 'read'] == sorted(alphagram_to_words['ader'])
    assert ['brag', 'grab'] == sorted(alphagram_to_words['abgr'])
