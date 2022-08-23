#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect

from app.app import app
from models import storage, Student


@app.route('/admin/students', methods=['POST'])
def create_student():
    """Creates a Level program."""
    first_name = request.form.get('first_name', None)
    last_name = request.form.get('last_name', None)
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    level_id = request.form.get('level_id', None)
    semester_id = request.form.get('semester_id', None)
    program_id = request.form.get('program_id', None)

    try:
        student = Student(first_name=first_name,
                      last_name=last_name,
                      email=email,
                      password=password,
                      program_id=program_id,
                      level_id=level_id,
                      semester_id=semester_id)

        storage.add(student)
        storage.save()
        flash('success')
    except ValueError as e:
        flash(str(e))
    except AttributeError as e:
        flash('something bad happened: attribute error')
    finally:
        return redirect(url_for('get_admin_page'))


@app.route('/admin/students')
def get_students():
    students = storage.all('Student')
    return render_template('admin/students.html', students=students)
