from flask import Flask

from app.corpus import Corpus
from app.routes.acknowledge_route import AcknowledgeRoute
from app.routes.primary_routes import AddWordsRoute, DeleteWordRoute, DeleteAllWordsRoute
from app.routes.primary_routes import AnagramsRoute
from app.routes.statistical_routes import MostAnagramsRoute
from app.routes.statistical_routes import StatsRoute


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle, methods=[route.method])


def create_app():
    app = Flask(__name__)
    corpus = Corpus()
    routes = [AcknowledgeRoute(),
              AddWordsRoute(corpus),
              AnagramsRoute(corpus),
              DeleteWordRoute(corpus),
              DeleteAllWordsRoute(corpus),
              StatsRoute(corpus),
              MostAnagramsRoute(corpus)]
    _set_up_routes(routes, app)

    return app
