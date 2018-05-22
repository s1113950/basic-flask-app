from flask import Blueprint

API = Blueprint('api', __name__, url_prefix='/api/')

import gack.web.api.user_notifications  # noqa
