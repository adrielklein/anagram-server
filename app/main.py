from app.corpus import Corpus
from app.routes.front_end_route import FrontEndRoute
from app.routes.primary_routes import AddWordsRoute, DeleteWordRoute, DeleteAllWordsRoute
from app.routes.primary_routes import AnagramsRoute
from app.routes.statistical_routes import MostAnagramsRoute
from app.routes.statistical_routes import StatsRoute
from flask import Flask


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle, methods=[route.method])


def create_app(words):
    app = Flask(__name__)
    corpus = Corpus(words)
    routes = [FrontEndRoute(),
              AddWordsRoute(corpus),
              AnagramsRoute(corpus),
              DeleteWordRoute(corpus),
              DeleteAllWordsRoute(corpus),
              StatsRoute(corpus),
              MostAnagramsRoute(corpus)]
    _set_up_routes(routes, app)

    return app
