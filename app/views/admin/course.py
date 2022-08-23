#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect, jsonify

from app.app import app
from models import storage, Course


@app.route('/admin/courses')
def get_courses():
    """return a list page of courses"""
    courses = storage.all('Course')
    return render_template('admin/courses.html', courses=courses)


@app.route('/admin/courses/<id_>')
def get_course(id_):
    """returns detail page of a single course"""
    course = storage.get('Course', id_)
    if not course:
        abort(404, 'Not Found')
    return render_template('admin/course.html', course=course)


@app.route('/admin/courses', methods=['POST'])
def create_course():
    """Creates a course"""
    name = request.form.get('name', None)
    course_code = request.form.get('course_code', None)

    if not name or not course_code:
        return jsonify({'message': 'name or course_code not present'}), 400

    course = Course(name=name, code=course_code)
    storage.add(course)
    storage.save()

    # return jsonify({'message': 'created succesfully'}), 201
    return redirect(url_for('get_admin_page'))


@app.route('/admin/courses/<id_>', methods=['DELETE'])
def delete_course(id_):
    """deletes a course"""
    course = storage.get('Course', id_)
    evaluated = storage.filter('StudentEvaluatedCourse',
                               course_id=id_)
    program_courses = storage.filter('ProgramCourse',
                               course_id=id_)
    if course:
        storage.remove(course)
        for eval_ in evaluated:
            storage.remove(eval_)
        for eval_ in program_courses:
            storage.remove(eval_)
        storage.save()
    
    return jsonify({'message': 'successful'}), 200


@app.route('/admin/courses/<id_>', methods=['PUT'])
def update_course(id_):
    """updates a course"""
    name = request.form.get('name', None)
    course_code = request.form.get('course_code', None)

    course = storage.get('Course', id_)
    if not Course:
        return jsonify({'message': 'Not Found'}), 404
    if name:
        course.name = name
    if course_code:
        course.code = course_code
    storage.save()

    return jsonify({'message': 'Updated succesfully'}), 200
