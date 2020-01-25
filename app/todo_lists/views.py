from flask_expects_json import expects_json
from flask import request, jsonify, current_app
from ..exceptions import DBException
from .models import TodoList


expected_request_body = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name']
}


def get_todo_lists():
    return jsonify(current_app.todo_lists.query())


@expects_json(expected_request_body)
def create_todo_list():
    return jsonify(current_app.todo_lists.add(TodoList(**request.json))), 201


def delete_todo_list(todo_id):
    items = current_app.todo_items.query(todo_list_id=todo_id)
    for item in items:
        current_app.todo_items.remove(item)

    message = 'Successfully deleted'
    try:
        current_app.todo_lists.remove(TodoList(id=todo_id))
    except DBException:
        message = 'Todo list already deleted'
    return {
        'status': 'success',
        'message': message
    }


@expects_json(expected_request_body)
def update_todo_list(todo_id):
    input_todo_list = TodoList(id=todo_id)
    try:
        updated_list = current_app.todo_lists.update(
            input_todo_list, TodoList(**request.json)
        )
        return jsonify(updated_list)
    except DBException as e:
        e.code = 400
        raise e
