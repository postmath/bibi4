from flask import (
    Blueprint, request
    )
from werkzeug.security import check_password_hash, generate_password_hash

from bibi4.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        db = get_db()
        error = None

        mapping = {'email': 'Email',
                   'fullname': 'Full name',
                   'password': 'Password',
                   }

        for key, description in mapping:
            if not request.form[key]:
                error = '{} is required.'.format(description)
                break

            if db.execute(
                    'SELECT id FROM user WHERE {} = ?'.format(key),
                    (request.form[key],)
                    ).fetchone() is not None:
                error = '{} {} is already registered.'
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user
