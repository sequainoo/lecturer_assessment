#!/usr/bin/python3
from flask import request, render_template, redirect, url_for, flash

from app.app import app
from helpers import get_student, log_into_session


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # make sure email and password are provided
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if not email or not password:
        flash('Provide email and password')
        return render_template('login.html')

    # validate email
    student = get_student(email=email)
    if not student:
        flash('Student with such email does not exist')
        return render_template('login.html')

    if not student.validate(password):
        flash('Password is not valid')
        return render_tempate('login.html')
    
    log_into_session(student.id)
    url = url_for('home') + '?' + 'token=' + student.id
    return redirect(url)
