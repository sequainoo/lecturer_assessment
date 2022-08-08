#!/usr/bin/python3
"""general question implementation"""

from models import Base, storage


class GeneralQuestion(Base):
    question = ''
 
    def __init__(self, **kwargs):
        if 'question' not in kwargs:
            raise AttributeError('question attr not provided')
        if type(kwargs['question']) is not str:
            raise TypeError('question must be a string')
        if not kwargs['question']:
            raise ValueError('question attr value cannot be empty')
        super().__init__(**kwargs)

    #@property
    #def answers(self):
     #   """returns the answers for each question"""
      #  return storage.filter('GeneralQuestionAnswer', general_question_id=self.id)
