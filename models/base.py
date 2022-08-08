#!/usr/bin/env python3
"""The base model of all classes"""

import uuid
from datetime import datetime
import json


class Base:
    
    def __init__(self, **kwargs):
        if 'id' in kwargs and 'created_at' in kwargs\
            and 'updated_at' in kwargs:
            for attr in kwargs:
                if attr == 'created_at' or attr == 'updated_at':
                    kwargs[attr] = datetime.fromisoformat(kwargs[attr])
                setattr(self, attr, kwargs[attr])
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def to_dict(self):
        """Converts object to json serializable form"""
        new_dict = {}
        for attr, value in self.__dict__.items():
            if type(value) is datetime:
                value = value.isoformat()
            new_dict[attr] = value
        return new_dict

    def to_json(self):
        """coverts to json string"""
        dict_ = self.to_dict()
        return json.dumps(dict_)
