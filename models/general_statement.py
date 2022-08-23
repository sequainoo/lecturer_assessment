#!/usr/bin/python3
"""general statements implementation"""

from models import Base, storage


class GeneralStatement(Base):
    text = ''
 
    def __init__(self, **kwargs):
        if 'text' not in kwargs:
            raise AttributeError('text  attrs not provided')
        if type(kwargs['text']) is not str:
            raise TypeError('text must be a string')
        if not kwargs['text']:
            raise ValueError('text attrs values cannot be empty')
        super().__init__(**kwargs)

    @property
    def options(self):
        """returns the answers or various options for each statement"""
        return storage.filter('GeneralStatementOption', general_statement_id=self.id)
