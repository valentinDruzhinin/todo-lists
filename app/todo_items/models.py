from dataclasses import dataclass, field
from datetime import datetime
from ..mixins import ToDBModelMixin, ModelSerializeMixin, ModelContentMixin


@dataclass
class TodoItem(ToDBModelMixin, ModelSerializeMixin, ModelContentMixin):
    id: str = ''
    text: str = ''
    due_date: datetime = field(default_factory=datetime.now)
    status: str = ''
    todo_list_id: str = ''

    @classmethod
    def from_db_object(cls, db_object):
        return cls(
            id=str(db_object['_id']),
            text=db_object['text'],
            due_date=datetime.fromisoformat(db_object['due_date']),
            status=db_object['status'],
            todo_list_id=db_object['todo_list_id']
        )
