from app.corpus import Corpus
from app.routes import RouteCreator
from flask import Flask


def create_app():
    app = Flask(__name__)
    corpus = Corpus()
    route_creator = RouteCreator(app, corpus)
    route_creator.set_up_routes()

    return app
