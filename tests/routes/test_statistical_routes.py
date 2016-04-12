import json
from unittest.mock import Mock

from app.corpus import Corpus


def test_when_stats_route_is_hit_then_call_stats_method(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'get_stats', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/stats')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['stats']

    Corpus.get_stats.assert_called_with()


def test_when_most_anagrams_route_is_hit_then_call_most_anagrams_method(app, monkeypatch):
    monkeypatch.setattr(Corpus, 'get_most_anagrams', Mock(return_value={'dgo': ['dog']}))
    with app.test_client() as test_client:
        response = test_client.get('/most')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert ['dog'] == json.loads(response_string)['dgo']

    Corpus.get_most_anagrams.assert_called_with()
