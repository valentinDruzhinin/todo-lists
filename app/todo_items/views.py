from flask_expects_json import expects_json
from flask import request, jsonify, current_app
from werkzeug.exceptions import BadRequest
from ..todo_lists.models import TodoList
from .models import TodoItem


expected_request_body = {
    'type': 'object',
    'properties': {
        'text': {'type': 'string'},
        'status': {'type': 'string'}
    },
    'required': ['text', 'status']
}


def get_todo_items(todo_id):
    todo_list_exists = current_app.todo_lists.query(**TodoList(id=todo_id).db_key())
    if todo_list_exists:
        return jsonify(current_app.todo_items.query(todo_list_id=todo_id))
    raise BadRequest(
        f'Unable to find todo list by given id="{todo_id}".'
    )


@expects_json(expected_request_body)
def create_todo_item(todo_id):
    todo_list_exists = current_app.todo_lists.query(**TodoList(id=todo_id).db_key())
    if todo_list_exists:
        new_item = current_app.todo_items.add(
            TodoItem(todo_list_id=todo_id, **request.json)
        )
        return jsonify(new_item), 201
    raise BadRequest(
        f'Unable to create todo item. Todo list with given id="{todo_id}" is missing.'
    )


@expects_json(expected_request_body)
def update_todo_item(todo_id, todo_item_id):
    todo_list_exists = current_app.todo_lists.query(**TodoList(id=todo_id).db_key())
    if todo_list_exists:
        input_item = TodoItem(id=todo_item_id)
        updated_item = current_app.todo_items.update(
            input_item,
            TodoItem(todo_list_id=todo_id, **request.json)
        )
        return jsonify(updated_item)
    raise BadRequest(
        f'Unable to update todo item. Todo list with given id="{todo_id}" is missing.'
    )


def delete_todo_item(todo_id, todo_item_id):
    todo_list_exists = current_app.todo_lists.query(**TodoList(id=todo_id).db_key())
    if todo_list_exists:
        return jsonify(current_app.todo_items.remove(
            TodoItem(id=todo_item_id, todo_list_id=todo_id)
        ))
    raise BadRequest(
        f'Unable to delete todo item. Todo list with given id="{todo_id}" is missing.'
    )
