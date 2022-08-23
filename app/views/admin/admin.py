#!/usr/bin/python3
from flask import render_template

from app.app import app
from models import storage


@app.route('/admin')
def get_admin_page():
    """return admin home page"""
    return render_template('admin/admin.html',
                           levels=storage.all('Level'),
                           semesters=storage.all('Semester'),
                           programs=storage.all('Program'),
                           courses=storage.all('Course'),
                           lecturers=storage.all('Lecturer'))
