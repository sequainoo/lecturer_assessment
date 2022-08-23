#!/usr/bin/env python3
"""This module defines a view function that return a page with 
forms to create evaluation categories/criteria, statements and questions.
"""
from flask import render_template

from app.app import  app
from models import storage

@app.route('/admin/evaluation-statements-creation-form')
def get_evaluation_statements_creation_form():
    criteria = storage.all('Criterion')
    criterion_options = storage.all('CriterionOption')
    general_statements = storage.all('GeneralStatement')
    general_questions = storage.all('GeneralQuestion')
    return render_template('admin/evaluation_statements_creation_form.html',
                           criterion_options=criterion_options,
                           criteria=criteria,
                           general_statements=general_statements,
                           general_questions=general_questions)
