from unittest.mock import Mock

from app.corpus import Corpus


def test_when_add_words_route_is_hit_then_add_words_to_corps(app):
    original_function = Corpus.add_words
    Corpus.add_words = Mock()
    with app.test_client() as test_client:
        response = test_client.post('/words.json', data=b'{ "words": ["read", "dear"] }')
        assert 201 == response.status_code

    Corpus.add_words.assert_called_with(['read', 'dear'])
    Corpus.add_words = original_function
