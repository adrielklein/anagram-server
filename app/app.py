from app.corpus import Corpus
from app.routes import AddWordsRoute, AcknowledgeRoute, AnagramsRoute, DeleteWordRoute
from flask import Flask


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle, methods=[route.method])


def create_app():
    app = Flask(__name__)
    corpus = Corpus()
    routes = [AcknowledgeRoute(),
              AddWordsRoute(corpus),
              AnagramsRoute(corpus),
              DeleteWordRoute(corpus)]
    _set_up_routes(routes, app)

    return app
