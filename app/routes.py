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
