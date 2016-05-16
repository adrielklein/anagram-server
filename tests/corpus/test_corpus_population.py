from app.corpus import Corpus


def test_when_initializing_corpus_with_words_then_add_them_to_corpus():
    corpus = Corpus(['read', 'dare'])
    ['dare'] == corpus.get_anagrams('read')
