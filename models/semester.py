#!/usr/bin/python3
from models import Base


class Semester(Base):
    semester = 1

    def __init__(self, **kwargs):
        if 'semester' not in kwargs:
            raise AttributeError('semester attr missing')
        if type(kwargs['semester']) is not int:
            raise TypeError('semester attr must be an int')
        if kwargs['semester'] < 1 or kwargs['semester'] > 2:
            raise ValueError('semester attr must be 1 or 2')
        self.semester = kwargs['semester']
        self.id = str(self.semester)
