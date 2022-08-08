#!/usr/bin/python3
"""Implementation of criterion f evaluation"""
from models import Base, storage


class Criterion(Base):
    name = ''

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise AttributeError('name attr not provided')
        if type(kwargs['name']) is not str:
            raise TypeError('name must be string')
        super().__init__(**kwargs)

    @property
    def statements(self):
        return storage.filter('CriterionStatement', criterion_id=self.id)
