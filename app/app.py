from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def acknowledge_route():
        return 'OK'

    return app
