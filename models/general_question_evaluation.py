#!/usr/bin/python3

from datetime import date

from models import Base


class GeneralQuestionEvaluation(Base):
    lecturer_id = ''
    course_id = ''
    general_question_id = ''
    student_id = ''
    year = 0
    semester_id = ''
    answer = ''

    def __init__(self, **kwargs):
        if 'lecturer_id' not in kwargs:
            raise AttributeError('lecturer_id, required attrs is not provided')
        if 'course_id' not in kwargs:
            raise AttributeError('course_id, required attrs not provided')
        if 'answer' not in kwargs:
            raise AttributeError('answer, required attrs not provided')
        if 'general_question_id' not in kwargs:
            raise AttributeError('general_question_id, required attrs not provided')
        if 'student_id' not in kwargs:
            raise AttributeError('student_id, required attrs not provided')
        if 'semester_id' not in kwargs:
            raise AttributeError('required attrs not provided')
        if type(kwargs['lecturer_id']) is not str\
            or type(kwargs['course_id']) is not str\
            or type(kwargs['answer']) is not str\
            or type(kwargs['general_question_id']) is not str\
            or type(kwargs['student_id']) is not str\
            or type(kwargs['semester_id']) is not str:
            raise TypeError('Wrong type of attrs values')
        if not kwargs['lecturer_id'] or not kwargs['course_id']\
            or not kwargs['answer'] or not kwargs['general_question_id']\
            or not kwargs['student_id'] or not kwargs['semester_id']:
            raise ValueError('Values cannot be empty')
        super().__init__(**kwargs)
        self.year = date.today().year

