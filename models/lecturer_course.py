#!/usr/bin/env python3
from models import Base, storage
import datetime


class LecturerCourse(Base):
    lecturer_id = ''
    course_id = ''

    def __init__(self, **kwargs):
        if 'lecturer_id' not in kwargs or 'course_id' not in kwargs:
            raise AttributeError('required attrs not provided')
        if type(kwargs['lecturer_id']) is not str:
            raise TypeError('name must be a str')
        if 'year' not in kwargs:
            kwargs['year'] = datetime.date.today().year


        # validate year
        year = kwargs['year']
        int(year)
        current_year = int(datetime.date.today().year)
        if int(year) < 1950 or int(year) > current_year + 4:
            raise ValueError('Not a valid year')

        super().__init__(**kwargs)
        #print(self.year)
