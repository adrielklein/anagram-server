from flask import request
import json


class AcknowledgeRoute(object):
    method = 'GET'
    path = '/'
    endpoint = 'acknowledge_route'

    def handle(self):
        return 'OK'


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
        result = {'anagrams': self._corpus.get_anagrams(word)}
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