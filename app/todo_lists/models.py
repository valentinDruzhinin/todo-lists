from dataclasses import dataclass
from ..mixins import ToDBModelMixin, ModelSerializeMixin, ModelContentMixin


@dataclass
class TodoList(ToDBModelMixin, ModelSerializeMixin, ModelContentMixin):
    id: str = ''
    name: str = ''

    @classmethod
    def from_db_object(cls, db_object):
        return cls(
            id=str(db_object['_id']),
            name=db_object['name']
        )
