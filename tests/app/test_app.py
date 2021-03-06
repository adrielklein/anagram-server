import json

from app import main
from app.main import create_app


def test_when_app_is_created_then_corpus_is_populated_with_english_dictionary():
    app = create_app(['dear', 'dare'])
    with app.test_client() as test_client:
        response = test_client.get('/anagrams/dear.json')
        response_string = response.get_data().decode()
        assert ['dare'] == sorted(json.loads(response_string)['anagrams'])