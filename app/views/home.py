#!/usr/bin/python3
import datetime

from flask import render_template, redirect, request, url_for

from app.app import app
from models import storage
from helpers import is_logged_in, login_expired, session_expiry_update


@app.route('/home')
def home():
    token = request.args.get('token', None)
    if not token or not is_logged_in(token)\
        or login_expired(token):
        return redirect(url_for('login'))

    session_expiry_update(token)

    student = storage.get('Student', token)
    return render_template('home.html',
                           student=student,
                           year=datetime.date.today().year,
                           token=token)

@app.route('/')
def also():
    token = request.args.get('token', None)
    if not token or not is_logged_in(token)\
        or login_expired(token):
        return redirect(url_for('login'))

    session_expiry_update(token)

    student = storage.get('Student', token)
    return render_template('home.html',
                           student=student,
                           year=datetime.date.today().year,
                           token=token)
