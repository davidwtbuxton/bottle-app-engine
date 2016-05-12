import logging
import os

import bottle
from google.appengine.api import users


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

# Add the email address of a Google account here.
ALLOWED_USERS = (
    'alice@example.com',
    'bob@example.net',
)


app = bottle.app()
log = logging.getLogger(__name__)


@app.route('/')
@app.route('/<filename:path>')
def home(filename='index.html'):
    user = users.get_current_user()
    is_admin = users.is_current_user_admin()

    log.debug('User %r', user)

    if user and (is_admin or (user.email() in ALLOWED_USERS)):
        return bottle.static_file(filename, root=STATIC_DIR)
    else:
        bottle.abort(404, 'File not found')
