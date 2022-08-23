#!/usr/bin/python3
from flask import request, flash, render_template, url_for, redirect

from app.app import app
from models import storage, Level


@app.route('/admin/levels', methods=['POST'])
def admin_create_level():
    """Creates a Level program."""
    level = request.form.get('level', None)

    if not level:
        flash('Provide all data')
        return redirect(url_for('get_admin_page'))

    try:
        level = Level(level=level)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('get_admin_page'))
    
    storage.add(level)
    storage.save()
    flash('successful')

    return redirect(url_for('get_admin_page'))
