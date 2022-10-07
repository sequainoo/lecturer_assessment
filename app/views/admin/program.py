#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect, jsonify

from app.app import app
from models import storage, Program


@app.route('/admin/programs')
def get_programs():
    """return a list page of programs"""
    programs = storage.all('Program')
    return render_template('admin/programs.html', programs=programs)


@app.route('/admin/programs/<id_>')
def get_program(id_):
    """returns detail page of a single program"""
    program = storage.get('Program', id_)
    courses = program.get_courses()
    if not program:
        abort(404, 'Not Found')
    return render_template('admin/program.html',
                           program=program,
                           courses=courses)


@app.route('/admin/programs', methods=['POST'])
def create_program():
    """Creates a program"""
    name = request.form.get('name', None)

    if not name:
        return jsonify({'message': 'name not present'}), 400
    name = name.title()
    program = storage.filter('Program', name=name)
    if not len(program):
        try:
           program = Program(name=name)
        except (TypeError) as e:
            flash('Must not start with a number or must not be a number')
        else:
            storage.add(program)
            storage.save()
            flash('success')
    else:
        flash('Already Exist')

    # return jsonify({'message': 'created succesfully'}), 201
    return redirect(url_for('get_admin_page'))


@app.route('/admin/programs/<id_>', methods=['DELETE'])
def delete_program(id_):
    """creates a criterion"""
    program = storage.get('Program', id_)
    if program:
        storage.remove(program)
        storage.save()
    
    return jsonify({'message': 'successful'}), 200


@app.route('/admin/programs/<id_>', methods=['PUT'])
def update_program(id_):
    """creates criterion statement"""
    name = request.form.get('name', None)

    if not name:
        return jsonify({'message': 'name not present'}), 400
    program = storage.get('Program', id_)
    if not program:
        return jsonify({'message': 'Not Found'}), 404
    program.name = name
    storage.save()

    return jsonify({'message': 'Updated succesfully'}), 200


#@app.route('/admin/program-creation-form')
#def get_program_creation_form():
#   return render_template('admin/program_creation.html')



@app.route('/admin/programs/<program_id>/courses/<course_id>',
           methods=['DELETE'])
def delete_course_from_program(program_id, course_id):
    """deletes course from program"""
    program = storage.get('Program', program_id)
    course = storage.get('Course', course_id)
    if program and course:
        program.remove_course(course)
    return jsonify({'message': 'success'}), 200
