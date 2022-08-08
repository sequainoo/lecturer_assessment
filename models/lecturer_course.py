#!/usr/bin/env python3
from models import Base, storage


class LecturerCourse(Base):
    lecturer_id = ''
    course_id = ''

    def __init__(self, **kwargs):
        if 'lecturer_id' not in kwargs or 'course_id' not in kwargs:
            raise AttributeError('required attrs not provided')
        if type(kwargs['lecturer_id']) is not str:
            raise TypeError('name must be a str')
        super().__init__(**kwargs)
