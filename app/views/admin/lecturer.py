#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect, jsonify

from app.app import app
from models import storage, Lecturer


@app.route('/admin/lecturers', methods=['POST'])
def create_lecturer():
    """Creates a Lecturer."""
    name = request.form.get('name', None)

    if not name:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    lecturer = Lecturer(name=name)
    flash('Success')
    storage.add(lecturer)
    storage.save()

    return redirect(url_for('get_admin_page'))


@app.route('/admin/lecturers/<id_>', methods=['DELETE'])
def delete_lecturer(id_):
    """Delete a lecturer."""

    lecturer = storage.get('Lecturer', id_)
    lecturer_courses = storage.filter('LecturerCourse',
                                      lecturer_id=id_)
    g_q_evals = storage.filter('GeneralQuestionEvaluation',
                               lecturer_id=id_)
    g_s_evals = storage.filter('GeneralStatementEvaluation',
                               lecturer_id=id_)
    c_evals = storage.filter('CriterionEvaluation',
                               lecturer_id=id_)
    std_eval_courses = []
    for lecturer_course in lecturer_courses:
        std_eval_courses.extend(
            storage.filter('StudentEvaluatedCourse',
                           course_id=lecturer_course.course_id)
        )

    for eval_ in g_q_evals:
        storage.remove(eval_)
    for eval_ in g_s_evals:
        storage.remove(eval_)
    for eval_ in c_evals:
        storage.remove(eval_)
    for eval_ in std_eval_courses:
        storage.remove(eval_)
    for eval_ in lecturer_courses:
        storage.remove(eval_)

    if lecturer:
        storage.remove(lecturer)
        storage.save()

    return redirect(url_for('get_admin_page'))


@app.route('/admin/lecturers/<id_>', methods=['PUT'])
def update_lecturer(id_):
    """Updates a lecturer."""
    name = request.form.get('name', None)

    if not name:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    lecturer = storage.get('Lecturer', id_)
    if lecturer:
        lecturer.name = name
        storage.save()

    return redirect(url_for('get_admin_page'))


@app.route('/admin/lecturers/<id_>')
def get_lecturer(id_):
    """Gets a lecturer and detail evaluations."""
    # Not Yet Implemented
    lecturer = storage.get('Lecturer', id_)
    if not lecturer:
        abort(404, 'not found')

    return render_template('admin/lecturer.html', lecturer=lecturer)


@app.route('/admin/lecturers')
def get_lecturers():
    """Gets a lecturers."""
    lecturers = storage.all('Lecturer')
    return render_template('admin/lecturers.html',
                           lecturers=lecturers)



@app.route('/admin/lecturers/<lecturer_id>/courses/<course_id>',
           methods=['DELETE'])
def remove_course_from_lecturer(lecturer_id, course_id):
    lecturer = storage.get('Lecturer', lecturer_id)
    course = storage.get('Course', course_id)

    if course and lecturer:
        lecturer.remove_course(course)
    return jsonify({'message': 'success'}), 200



@app.route('/admin/lecturers/<lecturer_id>/courses/<course_id>/evaluations')
def get_lecturer_evaluations(lecturer_id, course_id):
    lecturer = storage.get('Lecturer', lecturer_id)
    course = storage.get('Course', course_id)
    if not lecturer or not course:
        abort(404, 'not found')
    
    g_q_evals = lecturer.get_general_question_evaluations(course)
    g_s_evals, g_s_avg = lecturer.get_general_statement_evaluations(course)
    c_evals, c_evals_avg = lecturer.get_criterion_evaluations(course)
    total_avg = round((g_s_avg + c_evals_avg) / 2, 1)
    stars = int(total_avg)
    plus_half_star = False
    if total_avg % 1 >= 5:
        plus_half_star = True
    return render_template('admin/lecturer_evaluations.html',
                           lecturer=lecturer,
                           course=course,
                           total_avg=total_avg,
                           stars=stars,
                           plus_half_star=plus_half_star,
                           criterion_evaluations=c_evals,
                           general_statement_evaluations=g_s_evals,
                           general_question_evaluations=g_q_evals
                           )
