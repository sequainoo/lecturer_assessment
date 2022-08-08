#!/usr/bin/python3
from flask import redirect, request, url_for

from app.app import app
from models import storage
from helpers import is_logged_in, login_expired, session_expiry_update


@app.route('/home')
def home():
    token = request.params.get('token', None)
    if not token or not is_logged_in(token)\
        or login_expired(token):
        return redirect(url_for('login'))

    session_expiry_update(token)

    student = storage.get('Student', token)
    return render_template('home.html', {'student': student,
                                         'token': token})
