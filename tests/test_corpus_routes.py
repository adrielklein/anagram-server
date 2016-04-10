from unittest.mock import Mock

from app.corpus import Corpus
import json


def test_when_add_words_route_is_hit_then_add_words_to_corpus(app, monkeypatch):
    monkeypatch.setattr(Corpus, "add_words", Mock())
    with app.test_client() as test_client:
        response = test_client.post('/words.json', data=b'{ "words": ["read", "dear"] }')
        assert 201 == response.status_code

    Corpus.add_words.assert_called_with(['read', 'dear'])


def test_when_delete_word_route_is_hit_then_remove_word_from_corpus(app, monkeypatch):
    monkeypatch.setattr(Corpus, "get_anagrams", Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/anagrams/read.json')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['anagrams']

    Corpus.get_anagrams.assert_called_with('read')
