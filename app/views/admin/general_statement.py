#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect, jsonify

from app.app import app
from models import (storage, CriterionOption, Criterion,
                    CriterionStatement, GeneralStatement,
                    GeneralStatementOption)

@app.route('/admin/general-statements/options', methods=['POST'])
def create_general_statement_option():
    """Creates an option for criterion evaluation statements"""
    text = request.form.get('text', None)
    value = request.form.get('value', None)
    general_statement_id = request.form.get('general_statement_id', None)
    print(text,': ',  value, general_statement_id)

    if not text or not value or not general_statement_id:
        flash('provide all data')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    
    try:
        value = int(value)
    except (ValueError, TypeError):
        flash('Value should be an integer')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    if not storage.get('GeneralStatement', general_statement_id):
        flash('Provide existing statement')
        return redirect(url_for('get_evaluation_statements_creation_form'))
    
    option = GeneralStatementOption(general_statement_id=general_statement_id,
                                    text=text, value=value)
    storage.add(option)
    storage.save()
    flash('successfully created option')
    return redirect(url_for('get_evaluation_statements_creation_form'))
    
 
@app.route('/admin/general-statements/options/<id_>', methods=['DELETE'])
def delete_general_statement_option(id_):
    """deletes an option for criterion evaluation statements"""
    option = storage.get('GeneralStatementOption', id_)
    print(id_)
    if option:
        storage.remove(option)
        storage.save()
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200


@app.route('/admin/general-statements', methods=['POST'])
def create_general_statement():
    """creates criterion statement"""
    text = request.form.get('text', None)

    if not text:
        flash('Provide all data')
        return redirect(url_for('get_evaluation_statements_creation_form'))

    statement = GeneralStatement(text=text)
    storage.add(statement)
    storage.save()
    flash("Successful")
    return redirect(url_for('get_evaluation_statements_creation_form'))


@app.route('/admin/general-statements/<id_>', methods=['DELETE'])
def delete_general_statement(id_):
    """deletes an option for criterion evaluation statements"""
    statement = storage.get('GeneralStatement', id_)
    if statement:
        for option in statement.options:
            storage.remove(option)
        storage.remove(statement)
        storage.save()
    url = url_for('get_evaluation_statements_creation_form')
    return jsonify({'url': url}), 200
