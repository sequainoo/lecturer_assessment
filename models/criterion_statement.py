#!/usr/bin/python3
"""criterion statements implementation"""

from models import Base, storage


class CriterionStatement(Base):
    text = ''
    criterion_id = ''

    def __init__(self, **kwargs):
        if 'text' not in kwargs or 'criterion_id' not in kwargs:
            raise AttributeError('attrs required not provided')
        if type(kwargs['text']) is not str\
            or type('criterion_id') is not str:
            raise TypeError('wrong type of attr values')
        if not kwargs['text'] or not kwargs['criterion_id']:
            raise ValueError('attrs values cannot be empty')
        super().__init__(**kwargs)

    @property
    def criterion(self):
        return storage.filter('Criterion', id=self.criterion_id)
