#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect, jsonify

from app.app import app
from models import storage, GeneralQuestion


@app.route('/admin/general-questions', methods=['POST'])
def create_general_question():
    """creates a criterion"""
    question = request.form.get('question', None)

    if not question:
        flash('question should be provided')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    general_question = GeneralQuestion(question=question)
    storage.add(general_question)
    storage.save()
    flash('successfully created the criterion')
    return redirect(url_for('get_evaluation_statements_creation_form'))


@app.route('/admin/general-questions/<id_>', methods=['DELETE'])
def delete_general_question(id_):
    """creates a criterion"""
    question = storage.get('GeneralQuestion', id_)

    if question:
       storage.remove(question)
       storage.save()
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200
