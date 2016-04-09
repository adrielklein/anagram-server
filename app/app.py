from app.routes import acknowledge_route
from flask import Flask


def create_app():
    app = Flask(__name__)

    _set_up_routes(app)

    return app


def _set_up_routes(app):
    app.add_url_rule('/', 'acknowledge_route', acknowledge_route)
