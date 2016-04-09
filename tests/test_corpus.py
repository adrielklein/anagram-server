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
