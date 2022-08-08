#!/usr/bin/python3

from datetime import date

from models import Base


class GeneralStatementEvaluation(Base):
    lecturer_id = ''
    course_id = ''
    general_statement_id = ''
    general_statement_option_id = ''
    student_id = ''
    year = 0
    semester_id = ''

    def __init__(self, **kwargs):
        if 'lecturer_id' not in kwargs\
            or 'course_id' not in kwargs\
            or 'general_statement_id' not in kwargs\
            or 'general_statement_option_id' not in kwargs\
            or 'student_id' not in kwargs\
            or 'semester_id' not in kwargs:
            raise AttributeError('required attrs not provided')
        if type(kwargs['lecturer_id']) is not str\
            or type(kwargs['course_id']) is not str\
            or type(kwargs['general_statement_id']) is not str\
            or type(kwargs['general_statement_option_id']) is not str\
            or type(kwargs['student_id']) is not str\
            or type(kwargs['semester_id']) is not str:
            raise TypeError('Wrong type of attrs values')
        if not kwargs['lecturer_id'] or not kwargs['course_id']\
            or not kwargs['general_statement_id']\
            or not kwargs['general_statement_option_id']\
            or not kwargs['student_id'] or not kwargs['semester_id']:
            raise ValueError('Values cannot be empty')
        super().__init__(**kwargs)
        self.year = date.today().year

