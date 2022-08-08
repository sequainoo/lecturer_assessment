#!/usr/bin/python3
from datetime import datetime, timedelta

from models import storage
from app import session


def get_student(**kwargs):
    """Return a student by a attr like email or id"""
    students = storage.filter('Student', **kwargs)
    if len(students) > 0:
        return students[0]


def log_into_session(token):
    expiry_date = datetime.utcnow() + timedelta(minutes=30)
    session[token] = {'exp': expiry_date}


def is_logged_in(token):
    if token not in session:
        return False
    return True


def login_expired(token):
    now = datetime.utcnow()
    expiry_date = session[token]['exp']
    if now > expiry_date:
        return True
    return False


def session_expiry_update(token):
    session[token]['exp'] = datetime.utcnow() + timedelta(minutes=30)
