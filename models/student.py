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
            or 'semester_id' not in kwargs\
            or 'program_id' not in kwargs:
            raise AttributeError('attrs required not provided')
        if type(kwargs['first_name']) is not str\
            or type(kwargs['last_name']) is not str\
            or type(kwargs['semester_id']) is not str\
            or type(kwargs['email']) is not str\
            or type(kwargs['password']) is not str\
            or type(kwargs['level_id']) is not str\
            or type(kwargs['program_id']) is not str:
            raise TypeError('Attrs must be string')
        if not kwargs['first_name'] or not kwargs['last_name']\
            or not kwargs['semester_id'] or not kwargs['email']\
            or not kwargs['password'] or not kwargs['level_id']\
            or not kwargs['program_id']:
            raise ValueError('Provide all values')
        same_email_students = storage.filter('Student',
                                             email=kwargs['email'])
        if len(same_email_students):
            raise ValueError('email already in use')
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
    @property
    def unevaluated_courses(self):
        #current_courses = self.current_courses
        student_evaluated_courses = storage.filter('StudentEvaluatedCourse',
                                                   student_id=self.id)
        evaluated_courses = [storage.get('Course', obj.course_id)
                             for obj in student_evaluated_courses]
        print('\nevaluated', evaluated_courses, '\n' ,self.current_courses)
        return [course for course in self.current_courses
               if course[0] not in evaluated_courses]
        '''unevaluated = []
        for course in self.current_courses:
            print('\n', course.to_dict())
            if course not in evaluated_courses:
                unevaluated.append(course)
        #print(unevaluated)
        return unevaluated'''
    
    def validate(self, password):
        """validates a student password against a password input"""
        return self.password == password

    @property
    def lecturers(self):
        return [course.lecturer for course in self.program.courses]
