from unittest.mock import Mock

from app.corpus import Corpus
import json


def test_when_add_words_route_is_hit_then_add_words_to_corpus(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'add_words', Mock())
    with app.test_client() as test_client:
        response = test_client.post('/words.json', data=b'{ "words": ["read", "dear"] }')
        assert 201 == response.status_code

    Corpus.add_words.assert_called_with(['read', 'dear'])


def test_when_anagram_route_is_hit_then_get_anagrams(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'get_anagrams', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/anagrams/read.json')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['anagrams']

    Corpus.get_anagrams.assert_called_with('read', None)


def test_when_delete_word_route_is_hit_then_remove_word_from_corpus(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'remove_word', Mock())
    with app.test_client() as test_client:
        response = test_client.delete('/words/read.json')
        assert 200 == response.status_code

    Corpus.remove_word.assert_called_with('read')


def test_when_delete_all_words_route_is_hit_then_remove_all_words_from_corpus(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'clear', Mock())
    with app.test_client() as test_client:
        response = test_client.delete('/words.json')
        assert 204 == response.status_code

    Corpus.clear.assert_called_with()


def test_when_anagram_route_is_hit_with_limit_specified_then_get_anagrams_with_limit(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'get_anagrams', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/anagrams/read.json?limit=1')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['anagrams']

    Corpus.get_anagrams.assert_called_with('read', 1)
