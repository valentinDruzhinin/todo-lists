from app.mixins import DBActionsMixin
from .models import TodoList


class TodoListsRepository(DBActionsMixin):
    def __init__(self, db):
        super().__init__(TodoList, db)
        self._collection = self._db.todo_lists
