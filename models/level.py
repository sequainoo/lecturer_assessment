#!/usr/bin/env python3
"""a model of Level of student in school.
Also is a level a course is taught under a program
"""
from models import Base


class Level(Base):
    level = 100

    def __init__(self, **kwargs):
        if 'level' not in kwargs:
            raise AttributError('level attr not  provided')
        if type(kwargs['level']) is not int:
            try:
                kwargs['level'] = int(kwargs['level'])
            except ValueError:
                raise ValueError('level must be an integer')
        level = kwargs['level']
        # make sure level is patterned "100, 200, 300 ..."
        # it has to be divisible by 100
        # if 100 divides it it has to be from 1 to 9
        # and should not be a float ie a remainder
        if level < 100:
            raise ValueError('Not a valid level')
        if (level / 100) > 9 or (level % 100) != 0:
            raise ValueError('Not a valid level')
        self.level = level
        self.id = str(self.level)
