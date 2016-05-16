import json

from app.main import create_app, WordStore


def test_when_app_is_created_then_corpus_is_populated_with_english_dictionary(monkeypatch):
    monkeypatch.setattr(WordStore, 'get_words', lambda _: ['dear', 'dare'])
    app = create_app()
    with app.test_client() as test_client:
        response = test_client.get('/anagrams/dear.json')
        response_string = response.get_data().decode()
        assert ['dare'] == sorted(json.loads(response_string)['anagrams'])