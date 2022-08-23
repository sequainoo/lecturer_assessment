#!/usr/bin/python3
from flask import request, render_template, redirect, url_for, flash

from app.app import app
from helpers import get_student, logout_of_session


@app.route('/logout', methods=['GET'])
def logout():
    token = request.args.get('token', None)
    if token:
        logout_of_session(token)
    return render_template('login.html')
