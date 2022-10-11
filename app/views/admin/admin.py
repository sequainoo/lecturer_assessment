#!/usr/bin/python3
import datetime

from flask import render_template, request, url_for, redirect

from app.app import app
from models import storage
from helpers import log_admin_into_session, admin_is_logged_in, logout_admin


@app.route('/admin')
def get_admin_page():
    """return admin home page"""
    if not admin_is_logged_in():
        return render_template('admin/login.html')
    return render_template('admin/admin.html',
                           levels=storage.all('Level'),
                           semesters=storage.all('Semester'),
                           programs=storage.all('Program'),
                           courses=storage.all('Course'),
                           lecturers=storage.all('Lecturer'),
                           year=datetime.date.today().year)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    
    # make sure email and password are provided
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    if not username or not password:
        flash('username or password is not right')
        return render_template('admin/login.html')

    # validate 
    #admin = get_admin(username=username)
    #if not admin:
    #    flash('There is no such admin')
    #    return render_template('login.html')
    if username != 'admin':
        flash('Admin does not exist')
        return render_template('admin/login.html')
    if password != 'toor':
        flash('Authentication failed, You are not an admin')
        return render_template('admin/login.html')

    #if not student.validate(password):
    #    flash('Password is not valid')
    #    return render_template('login.html')
    
    log_admin_into_session()
    url = url_for('get_admin_page')
    return redirect(url)

@app.route('/admin/logout')
def admin_logout():
    logout_admin()
    return redirect(url_for('admin_login'))
