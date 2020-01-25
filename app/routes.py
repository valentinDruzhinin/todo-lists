from .todo_lists import views as lists_views
from .todo_items import views as items_views


class Route:
    def __init__(self, url, view, **params):
        self.url = url
        self.view = view
        self.params = params


ROUTES = (
    Route('/todo_lists', lists_views.get_todo_lists, methods=('GET',)),
    Route('/todo_lists', lists_views.create_todo_list, methods=('POST',)),
    Route('/todo_lists/<todo_id>', lists_views.delete_todo_list, methods=('DELETE',)),
    Route('/todo_lists/<todo_id>', lists_views.update_todo_list, methods=('PUT',)),
    Route('/todo_lists/<todo_id>/todo_items', items_views.get_todo_items, methods=('GET',)),
    Route('/todo_lists/<todo_id>/todo_items', items_views.create_todo_item, methods=('POST',)),
    Route('/todo_lists/<todo_id>/todo_items/<todo_item_id>', items_views.update_todo_item, methods=('PUT',)),
    Route('/todo_lists/<todo_id>/todo_items/<todo_item_id>', items_views.delete_todo_item, methods=('DELETE',)),
)
