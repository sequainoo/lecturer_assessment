#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect

from app.app import app
from models import storage, ProgramCourse


@app.route('/admin/program-course', methods=['POST'])
def create_program_course():
    """Creates a program course which in turn creates a course for program."""
    program_id = request.form.get('program_id', None)
    course_id = request.form.get('course_id', None)
    level_id = request.form.get('level_id', None)
    semester_id = request.form.get('semester_id', None)

    if not program_id or not course_id or not level_id or not semester_id:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    if not storage.get('Program', program_id)\
        or not storage.get('Course', course_id)\
        or not storage.get('Level', level_id)\
        or not storage.get('Semester', semester_id):
        flash('Provide Valid data')
        return redirect(url_for('get_admin_page'))

    program_course = ProgramCourse(program_id=program_id,
                            course_id=course_id,
                            level_id=level_id,
                            semester_id=semester_id)
    print('can i see this')
    storage.add(program_course)
    storage.save()
    
    flash('success')
    return redirect(url_for('get_admin_page'))
