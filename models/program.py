#!/usr/bin/python3

from models import Base
from models import Course, Level, Semester, ProgramCourse, storage


class Program(Base):
    name = ''
    courses = []
    
    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise ValueError('Must provide a name of program')
        if type(kwargs['name']) is not str:
            raise TypeError('name must be str')
        super().__init__(**kwargs)

    def get_courses(self, **kwargs):
        """Returns a list of courses under this program.
        search in program courses for courses whose program id is
        this programs id
        [(course_obj, level_obj, semester_obj)...]
        """
        program_course_list = storage.filter('ProgramCourse',
                                             program_id=self.id,
                                             **kwargs)
        course_list = [(storage.get('Course', program_course.course_id),
                        storage.get('Level', program_course.level_id),
                        storage.get('Semester', program_course.semester_id))
                       for program_course in program_course_list]
        return course_list

    def add_course(self, course=None, level=None, semester=None):
        """adds a course to the program,
        arguments:
            course :(models.Course) a course of the program
            level :(models.Level): level that the course applies
            semester : a semester that the course applies
        """
        if course is None or level is None or semester is None:
            raise ValueError('Provide value(s)')
        if type(course) is not Course or type(Level) is not Level\
            or type(semester) is not Semester:
                raise TypeError('Wrong type(s)!')
        program_course = ProgramCourse(course_id=course.id,
                                       program_id=self.id,
                                       level_id=level.id,
                                       semester_id=semester.id)
