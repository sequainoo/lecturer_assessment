#!/usr/bin/python3
from models import Base


class CriterionOption(Base):
    text = ''
    value = 0

    def __init__(self, **kwargs):
        if 'text' not in kwargs or 'value' not in kwargs:
            raise AttributeError('attrs not provided')
        if type(kwargs['text']) is not str\
            or type(kwargs['value']) is not int:
            raise TypeError('Wrong type of values')
        self.text = kwargs['text']
        self.value = kwargs['value']
        if 'id' in kwargs and type(kwargs['id']) is str:
            self.id = kwargs['id']
        else:
            self.id = str(self.value)
