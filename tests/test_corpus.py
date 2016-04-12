def test_when_requesting_anagram_and_no_words_are_in_corpus_then_get_back_empty_list(corpus):
    assert [] == corpus.get_anagrams('read')


def test_when_requesting_anagram_of_read_then_get_dear(corpus):
    corpus.add_words(['read', 'dear'])
    assert ['dear'] == corpus.get_anagrams('read')


def test_when_requesting_anagram_of_dear_then_get_read(corpus):
    corpus.add_words(['read', 'dear'])
    assert ['read'] == corpus.get_anagrams('dear')


def test_when_word_gets_deleted_then_remove_it_from_data_store(corpus):
    corpus.add_words(['read', 'dear'])
    corpus.remove_word('read')
    assert [] == corpus.get_anagrams('dear')


def test_when_all_words_get_removed_then_data_store_is_empty(corpus):
    corpus.add_words(['read', 'dear'])
    corpus.clear()
    assert [] == corpus.get_anagrams('read')


def test_when_duplicate_words_get_added_then_ignore_them(corpus):
    corpus.add_words(['read', 'dear', 'dear'])
    assert ['dear'] == corpus.get_anagrams('read')


def test_when_removing_non_existant_word_then_do_nothing_and_do_not_error(corpus):
    corpus.remove_word('read')


def test_when_limit_is_specified_for_maximum_number_of_anagrams_then_do_not_exceed_limit(corpus):
    corpus.add_words(['read', 'dear'])
    assert [] == corpus.get_anagrams('read', limit=0)


def test_when_requesting_anagrams_of_words_that_are_not_in_corpus_yet_then_return_nothing(corpus):
    corpus.add_words(['read'])
    assert [] == corpus.get_anagrams('dare')


def test_when_stats_method_is_called_then_return_stats(corpus):
    corpus.add_words(['it', 'dog', 'person'])
    stats = corpus.get_stats()
    assert 5 == len(stats)
    assert 3 == stats['count']
    assert 2 == stats['min_length']
    assert 6 == stats['max_length']
    assert 3 == stats['med_length']
    assert 11 / 3 == stats['ave_length']


def test_when_stats_method_is_called_with_no_words_then_return_stats(corpus):
    stats = corpus.get_stats()
    assert 5 == len(stats)
    assert 0 == stats['count']
    assert 0 == stats['min_length']
    assert 0 == stats['max_length']
    assert 0 == stats['med_length']
    assert 0 == stats['ave_length']


def test_when_most_anagrams_method_is_called_then_words_with_most_anagrams(corpus):
    corpus.add_words(['read', 'dare'])
    corpus.add_words(['brag', 'grab'])
    corpus.add_words(['it'])
    alphagram_to_words = corpus.get_most_anagrams()
    assert 2 == len(alphagram_to_words)
    assert ['dare', 'read'] == sorted(alphagram_to_words['ader'])
    assert ['brag', 'grab'] == sorted(alphagram_to_words['abgr'])


def test_when_there_are_no_words_then_get_empty_hash_table(corpus):
    alphagram_to_words = corpus.get_most_anagrams()
    assert 0 == len(alphagram_to_words)
