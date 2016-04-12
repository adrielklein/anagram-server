from flask import request
import json


class AddWordsRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'POST'
    path = '/words.json'
    endpoint = 'add_words_route'

    def handle(self):
        words = json.loads(request.get_data().decode())['words']
        self._corpus.add_words(words)
        return '', 201


class AnagramsRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'GET'
    path = '/anagrams/<word>.json'
    endpoint = 'anagrams_route'

    def handle(self, word):
        limit = None if request.args.get('limit') is None else int(request.args.get('limit'))
        result = {'anagrams': self._corpus.get_anagrams(word, limit)}
        return json.dumps(result)


class DeleteWordRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'DELETE'
    path = '/words/<word>.json'
    endpoint = 'delete_word_route'

    def handle(self, word):
        self._corpus.remove_word(word)
        return 'OK'


class DeleteAllWordsRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'DELETE'
    path = '/words.json'
    endpoint = 'delete_all_words_route'

    def handle(self):
        self._corpus.clear()
        return 'OK', 204
