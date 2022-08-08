#!/usr/bin/env python3
from models import Base, storage


class Student(Base):
    first_name = ''
    last_name = ''
    email = ''
    password = ''
    level_id =''
    semester_id = ''
    program_id = ''
    # commence_year = 0
    # commence_month = 0
    # end_year = 0
    # end_month = 0

    def __init__(self, **kwargs):
        if 'first_name' not in kwargs\
            or 'last_name' not in kwargs\
            or 'password' not in kwargs\
            or 'email' not in kwargs\
            or 'level_id' not in kwargs\
            or 'semeser_id' not in kwargs\
            or 'program_id' not in kwargs:
            raise AttributeError('attrs required not provided')
        if type(kwargs['first_name']) is not str\
            or type(kwargs['last_name']) is not str\
            or type(kwargs['username']) is not str\
            or type(kwargs['email']) is not str\
            or type(kwargs['password']) is not str\
            or type(kwargs['level_id']) is not str\
            or type(kwargs['program_id']) is not str:
            raise TypeError('Attrs must be string')
        super().__init__(**kwargs)
    
    @property
    def program(self):
        return storage.get('Program', self.program_id)

    @property
    def level(self):
        return storage.get('Level', self.level_id)

    @property
    def semester(self):
        return storage.get('Semester', self.semester_id)

    @property
    def courses(self):
        return self.program.get_courses()

    @property
    def current_courses(self):
        return self.program.get_courses(semester_id=self.semester_id,
                                        level_id=self.level_id)
    
    def validate(self, password):
        """validates a student password against a password input"""
        return self.password == password

    @property
    def lecturers(self):
        return [course.lecturer for course in self.program.courses]
