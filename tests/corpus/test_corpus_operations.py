def test_when_requesting_anagram_and_no_words_are_in_corpus_then_get_back_empty_list(corpus):
    assert [] == corpus.get_anagrams('read')


def test_when_requesting_anagram_of_read_then_get_dear(corpus):
    corpus.add_words(['read', 'dear'])
    assert ['dear'] == corpus.get_anagrams('read')


def test_when_requesting_anagram_of_uppercase_read_then_get_dear(corpus):
    corpus.add_words(['read', 'dear'])
    assert ['dear'] == corpus.get_anagrams('Read')


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
