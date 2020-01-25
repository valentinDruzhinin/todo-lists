import json
from bson import ObjectId
from pymongo import ReturnDocument
from .exceptions import DBException


class DBActionsMixin:
    def __init__(self, model, db):
        self._model_cls = model
        self._db = db

    def add(self, item):
        db_obj = self._collection.insert_one(item.prepare_for_db())
        model = self._model_cls(id=str(db_obj.inserted_id))
        return self.query(**model.db_key()).pop()

    def query(self, **query_params):
        return [
            self._model_cls.from_db_object(db_obj) for db_obj in self._collection.find(query_params)
        ]

    def remove(self, todo_item):
        db_obj = self._collection.find_one_and_delete(todo_item.db_key())
        if db_obj:
            return self._model_cls.from_db_object(db_obj)
        raise DBException(f'Unable to remove. Object with id={todo_item.id} is absent.')

    def update(self, old_todo_item, new_todo_item):
        if not self.query(**old_todo_item.db_key()):
            raise DBException(f'Unable to update. Object with id={old_todo_item.id} is absent.')
        db_obj = self._collection.find_one_and_update(
            old_todo_item.db_key(),
            {'$set': new_todo_item.prepare_for_db(with_empty_fields=False)},
            return_document=ReturnDocument.AFTER
        )
        return self._model_cls.from_db_object(db_obj)


class ToDBModelMixin:
    def prepare_for_db(self, with_empty_fields=True):
        obj = vars(self)
        del obj['id']
        filter_func = lambda x: True if with_empty_fields else lambda x: x
        obj = {key: str(value) for key, value in obj.items() if filter_func(value)}
        return obj

    def db_key(self):
        return {'_id': ObjectId(self.id)}


class ModelSerializeMixin:
    def __str__(self):
        return json.dumps(self)


class ModelContentMixin:

    @property
    def is_empty(self):
        return not bool([v for v in vars(self).values() if v])
