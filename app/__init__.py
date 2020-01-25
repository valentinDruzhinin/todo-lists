from flask import Flask
from flask_pymongo import PyMongo
from .exceptions_handler import register_exceptions_handler
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    register_repositories(app, PyMongo(app).db)
    register_routes(app)
    register_exceptions_handler(app)
    return app


def register_repositories(app, db):
    from .todo_lists.repository import TodoListsRepository
    from .todo_items.repository import TodoItemsRepository
    app.todo_lists = TodoListsRepository(db)
    app.todo_items = TodoItemsRepository(db)


def register_routes(app):
    from .routes import ROUTES
    for route in ROUTES:
        app.route(route.url, **route.params)(route.view)
