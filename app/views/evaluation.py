#!/usr/bin/python3
from flask import request, redirect, url_for

from app.app import app
from models import storage
from helpers import is_logged_in, login_expired, session_expiry_update


@app.route('/evaluate/<course_id:str>')
def evaluate(course_id):
    token = request.params.get('token', None)
    if not token or not is_logged_in(token) or login_expired(token):
        return redirect(url_for('login'))
    session_expiry_update(token)

    course = storage.get('Course', course_id)
    if not course:
        # redirect to student page
        url = url_for('home') '?' + 'token=' + token
        return redirect(url)
    student = storage.get('Student' ,token)

    # return evaluation form
    criteria = storage.all('Criterion')
    criterion_options = storage.all('CriterionOption')
    general_statements = storage.all('GeneralStatement')
    general_questions = storage.all('GeneralQuestion')
    
    return render_template('evaluation_form.html', {'criteria': criteria,
                                                    'criterion_options': criterion_options,
                                                    'general_statements': general_statements,
                                                    'general_questions': general_questions,
                                                    'student': student,
                                                    'course': course,
                                                    'token': token})
