import dataclasses

from flask import (
    Blueprint, request, redirect, url_for, flash, render_template
    )
from werkzeug.security import check_password_hash, generate_password_hash

from bibi4.db import get_db
from bibi4.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        db = get_db()
        error = None

        values = {}
        
        for field in dataclasses.fields(User):
            if field.metadata.get('skip', False):
                continue

            description = field.metadata.get('description') or field.name
            
            if not request.form[field.name]:
                error = '{} is required.'.format(description)
                break

            value = request.form[field.name]
            
            if request.metadata.get('unique') and db.execute(
                    'SELECT id FROM user WHERE {} = ?'.format(field.name),
                    (value,)).fetchone() is not None:
                error = '{} {} is already registered.'.format(description, value)

            values[field.name] = value

        if error is None:
            fieldnames = ', '.join(values.keys())
            qmarks = ', '.join('?' * len(values))
            to_fill_out = tuple(values.values())
            db.execute('INSERT INTO user ({}) VALUES ({})'.format(fieldnames, qmarks), to_fill_out)
            db.commit()
            return redirect(url_for('auth.login'))
        
        else:
            flash(error)
            # fall through

    return render_template('auth/register.html')
