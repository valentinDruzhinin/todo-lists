from pymongo import ReturnDocument
from bson import ObjectId
from flask import request, jsonify, current_app


def todo_lists():
    todos = current_app.db.tododb
    if request.method == 'POST':
        todos.insert({'name': request.json.get('name')})
        return {'name': request.form.get('name')}
    if request.method == 'GET':
        return jsonify([
            {
                'id': str(todo['_id']),
                'name': todo['name']
            } for todo in todos.find()
        ])


def todo_list(todo_id):
    todos = current_app.db.tododb
    if request.method == 'DELETE':
        todo = todos.find_one_and_delete({'_id': ObjectId(todo_id)})
        if todo:
            return 'Successfully deleted!'
    if request.method == 'PUT':
        updated_todo = todos.find_one_and_update(
            {'_id': ObjectId(todo_id)},
            {'$set': {'name': request.json.get('name')}},
            return_document=ReturnDocument.AFTER
        )
        if updated_todo:
            return {
                'id': str(updated_todo['_id']),
                'name': updated_todo['name']
            }
    return f'Unable to find todo list by given id={todo_id}', 404
