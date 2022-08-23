#!/usr/bin/python3
from datetime import datetime

from flask import render_template, request, redirect, url_for, jsonify

from app.app import app
from models import (storage, GeneralQuestionEvaluation,
                    GeneralStatementEvaluation, CriterionEvaluation,
                    StudentEvaluatedCourse)
from helpers import is_logged_in, login_expired, session_expiry_update


@app.route('/evaluate/<course_id>')
def get_evaluation_form(course_id):
    token = request.args.get('token', None)
    if not token or not is_logged_in(token) or login_expired(token):
        return redirect(url_for('login'))
    session_expiry_update(token)

    course = storage.get('Course', course_id)
    if not course:
        # redirect to student page
        url = url_for('home') + '?' + 'token=' + token
        return redirect(url)
    student = storage.get('Student' ,token)

    # return evaluation form
    criteria = storage.all('Criterion')
    criterion_options = storage.all('CriterionOption')
    general_statements = storage.all('GeneralStatement')
    general_questions = storage.all('GeneralQuestion')
    
    return render_template('evaluation_form.html',
                           criteria=criteria,
                           criterion_options=criterion_options,
                           general_statements=general_statements,
                           general_questions=general_questions,
                           student=student,
                           course=course,
                           lecturer=course.lecturer,
                           year=datetime.utcnow().year,
                           token=token)


@app.route('/evaluate/<course_id>', methods=['POST'])
def evaluate(course_id):
    data = request.get_json()
    for key, datasets in data.items():
        if key == 'criteriaDatasets':
            for dataset in datasets:
                storage.add(CriterionEvaluation(**dataset))
        elif key == 'statementsDatasets':
            for dataset in datasets:
                storage.add(GeneralStatementEvaluation(**dataset))
        elif key == 'answersDatasets':
            for dataset in datasets:
                storage.add(GeneralQuestionEvaluation(**dataset))
    course = storage.get('Course', course_id)
    stdnt_eval_c = StudentEvaluatedCourse(course_id=course.id,
                                          student_id=request.args.get('token', None))
    storage.add(stdnt_eval_c)
    storage.save()
    url = url_for('home') + '?' + 'token=' + request.args.get('token', None)
    return jsonify({'success': 'evaluated', 'url': url}), 200
