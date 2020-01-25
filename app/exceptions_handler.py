from flask import json, Response


def register_exceptions_handler(app):

    @app.errorhandler(Exception)
    def handle_exception(e):
        status_code = getattr(e, 'code', None) or 500
        error_name = getattr(e, 'name', None) or e.__class__.__name__
        error_description = str(
            getattr(e, 'description', None) or e
        )

        response = Response(status=status_code)
        response.data = json.dumps({
            "code": status_code,
            "name": error_name,
            "description": error_description,
        })
        response.content_type = "application/json"
        return response
