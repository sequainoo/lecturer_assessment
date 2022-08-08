#!/usr/bin/env python3
"""a course that a student takes under a progam
a course can be under one or more programs
"""
from models import Base, storage


class Course(Base):
    name = ''
    course_code = ''

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise AttributeError('Missing Attribute name')
        if type(kwargs['name']) is not str:
            raise TypeError('name attr must be a str')
        super().__init__(**kwargs)

    @property
    def lecturer(self):
        """return the associated lecturer of a course"""
        lecturer_course = storage.filter('LecturerCourse',
                                         course_id=self.id)
        lecturer_id = lecturer_course[0].lecturer_id
        return storage.get('Lecturer', lecturer_id)
