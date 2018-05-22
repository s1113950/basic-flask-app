import traceback

from flask import Flask
from gack.web.api import API  # noqa

app = Flask(__name__)


# Register blueprint(s)
app.register_blueprint(API)


@app.errorhandler(404)
def not_found(error):
    """
    Handler for missing pages.
    """
    return "Page not found", 404


@app.errorhandler(Exception)
def global_exception_handler(e):
    print(traceback.format_exc())
    return "Unknown Error", 500
