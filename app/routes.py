from .todo_lists.views import todo_lists, todo_list


class Route:
    def __init__(self, url, view, **params):
        self.url = url
        self.view = view
        self.params = params


ROUTES = (
    Route('/todo_lists', todo_lists, methods=('GET', 'POST')),
    Route('/todo_lists/<todo_id>', todo_list, methods=('DELETE', 'PUT')),
)
