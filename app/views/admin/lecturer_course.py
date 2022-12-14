#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect

from app.app import app
from models import storage, LecturerCourse


@app.route('/admin/lecturer-course', methods=['POST'])
def create_lecturer_course():
    """Creates a LecturerCourse which in turn creates a course
    for lecturer.
    """
    lecturer_id = request.form.get('lecturer_id', None)
    course_id = request.form.get('course_id', None)
    year = request.form.get('year', None)

    if not course_id or not lecturer_id or not year:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    if not storage.get('Lecturer', lecturer_id)\
        or not storage.get('Course', course_id):
        flash('Provide Valid data')
        return redirect(url_for('get_admin_page'))

    try:
        lecturer_course = LecturerCourse(lecturer_id=lecturer_id,
                                         course_id=course_id,
                                         year=year)
        storage.add(lecturer_course)
        storage.save()
        flash('success')
    except (ValueError) as e:
        flash(str(e))

    return redirect(url_for('get_admin_page'))
