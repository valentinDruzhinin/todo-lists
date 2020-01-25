from app.mixins import DBActionsMixin
from .models import TodoItem


class TodoItemsRepository(DBActionsMixin):
    def __init__(self, db):
        super().__init__(TodoItem, db)
        self._collection = self._db.todo_items
