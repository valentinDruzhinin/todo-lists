from flask import Flask
from .config import Config
from flask_pymongo import PyMongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.db = PyMongo(app).db

    from .routes import ROUTES
    for route in ROUTES:
        app.route(route.url, **route.params)(route.view)

    return app
