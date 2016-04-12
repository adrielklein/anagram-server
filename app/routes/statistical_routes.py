import json


class StatsRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'GET'
    path = '/stats'
    endpoint = 'stats_route'

    def handle(self):
        result = {'stats': self._corpus.get_stats()}
        return json.dumps(result)


class MostAnagramsRoute(object):
    def __init__(self, corpus):
        self._corpus = corpus

    method = 'GET'
    path = '/most'
    endpoint = 'most'

    def handle(self):
        return json.dumps(self._corpus.get_most_anagrams())
