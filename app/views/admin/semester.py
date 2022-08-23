#!/usr/bin/python3
from flask import request, flash, url_for, redirect

from app.app import app
from models import storage, Semester


@app.route('/admin/semesters', methods=['POST'])
def admin_create_semester():
    """Creates a Semester."""
    semester = request.form.get('semester', None)

    if not semester:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    try:
        semester = Semester(semester=semester)
        storage.add(semester)
        storage.save()
        flash('Success')
    except ValueError as e:
        flash('Must be a number')
    finally:
        return redirect(url_for('get_admin_page'))
