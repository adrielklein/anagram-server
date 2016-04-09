from flask import request
import json


class RouteCreator(object):
    def __init__(self, app, corpus):
        self.app = app
        self._corpus = corpus

    def set_up_routes(self):
        self.app.add_url_rule('/', 'acknowledge_route', self._acknowledge_route)
        self.app.add_url_rule('/words.json', 'add_words_route', self._add_words_route, methods=['POST'])

    def _acknowledge_route(self):
        return 'OK'

    def _add_words_route(self):
        words = json.loads(request.get_data().decode())['words']
        self._corpus.add_words(words)
        return '', 201
