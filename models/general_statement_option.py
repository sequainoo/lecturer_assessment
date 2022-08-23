#!/usr/bin/python3
from models import Base


class GeneralStatementOption(Base):
    text = ''
    value = 0
    general_statement_id = 0

    def __init__(self, **kwargs):
        if 'text' not in kwargs or 'general_statement_id' not in kwargs\
            or 'value' not in kwargs:
            raise TypeError('Called without right type of attrs')
        if type(kwargs['text']) is not str\
            or type(kwargs['general_statement_id']) is not str:
            raise TypeError('Wrong type of values')
        kwargs['value'] = int(kwargs['value'])
        super().__init__(**kwargs)
