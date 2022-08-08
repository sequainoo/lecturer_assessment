#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect

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
