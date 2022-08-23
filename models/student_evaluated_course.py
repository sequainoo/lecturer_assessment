#!/usr/bin/python3

from models import Base


class StudentEvaluatedCourse(Base):
    student_id = ''
    course_id = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
