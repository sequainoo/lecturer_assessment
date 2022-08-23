#!/usr/bin/python3
from flask import (request, flash, render_template, url_for, redirect, abort,
                   jsonify)

from app.app import app
from models import storage, CriterionOption, Criterion, CriterionStatement


@app.route('/admin/criterion-options', methods=['POST'])
def create_criterion_option():
    """Creates an option for criterion evaluation statements"""
    text = request.form.get('text', None)
    value = request.form.get('value', None)

    if not text or not value:
        flash('provide all data')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    
    try:
        value = int(value)
    except (ValueError, TypeError):
        flash('Value should be an integer')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    
    criterion_option = CriterionOption(text=text, value=value)
    storage.add(criterion_option)
    storage.save()
    flash('successfully created criterion option')
    return redirect(url_for('get_evaluation_statements_creation_form'))


@app.route('/admin/criterion-options/<id_>', methods=['DELETE'])
def delete_criterion_option(id_):
    obj = storage.get('CriterionOption', id_)
    if not obj:
        print('******************not found**************')
    if obj:
        storage.remove(obj)
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200


@app.route('/admin/criteria', methods=['POST'])
def create_criterion():
    """creates a criterion"""
    name = request.form.get('name', None)

    if not name:
        flash('name should be provided')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    criterion = Criterion(name=name)
    storage.add(criterion)
    storage.save()
    flash('successfully created the criterion')
    return redirect(url_for('get_evaluation_statements_creation_form'))


@app.route('/admin/criteria/<id_>', methods=['DELETE'])
def delete_criterion(id_):
    obj = storage.get('Criterion', id_)
    if obj:
        for statement in obj.statements:
            storage.remove(statement)
        storage.remove(obj)
        storage.save()
    flash('Successfully Deleted')
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200


@app.route('/admin/criterion-statements', methods=['POST'])
def create_criterion_statement():
    """creates criterion statement"""
    criterion_id = request.form.get('criterion_id', None)
    text = request.form.get('text', None)

    if not criterion_id or not text:
        flash('Provide all data')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    if not storage.get('Criterion', criterion_id):
        flash("Provide a valid criteria")
        return redirect(url_for('get_evaluation_statements_creation_form'))

    statement = CriterionStatement(criterion_id=criterion_id,
                                   text=text)
    storage.add(statement)
    storage.save()
    flash("Successful")
    return redirect(url_for('get_evaluation_statements_creation_form'))


@app.route('/admin/criterion-statements/<id_>', methods=['DELETE'])
def delete_criterion_statement(id_):
    obj = storage.get('CriterionStatement', id_)
    if obj:
        storage.remove(obj)
        storage.save()
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200
