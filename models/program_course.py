#!/usr/bin/env python3
"""intermediary model for programs and courses.
Linking programs and courses together by their ids
"""
from models import Base, storage


class ProgramCourse(Base):
    program_id = ''
    course_id = ''
    level_id = ''
    semester_id = ''

    def __init__(self, **kwargs):
        # check that all required attrs are provided
        if 'program_id' not in kwargs or 'course_id' not in kwargs\
            or 'level_id' not in kwargs or 'semester_id' not in kwargs:
            raise AttributeError('Provide the right attributes')
        # check that the related objects are valid
        #if not storage.get('Program', kwargs['program_id']):
         #   raise ValueError('Program with such id does not exist')
        #if not storage.get('Course', kwargs['course_id']):
        #    raise ValueError('Course with such id does not exist')
        #if not storage.get('Level', kwargs['level_id']):
        #    raise ValueError('Level with such id does not exist')
        #if not storage.get('Semester', kwargs['semester_id']):
        #    raise ValueError('Semester with such id does not exist')
        # create and init obj if no problem
        super().__init__(**kwargs)
