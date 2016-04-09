from app.routes import RouteCreator
from flask import Flask


def create_app():
    app = Flask(__name__)
    route_creator = RouteCreator(app)
    route_creator.set_up_routes()

    return app
