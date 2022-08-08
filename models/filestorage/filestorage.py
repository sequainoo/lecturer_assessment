#!/usr/bin/env python3
"""Storage abstraction for objects of the program"""
import os
import json

from models import classes # classes is a hashmap of classnames and classes


class Storage:
    __store = {}
    __filename = 'db.json'

    def __init__(self):
        for classname in classes.keys():
            Storage.__store[classname] = {}

    def all(self, classname):
        if type(classname) is not str:
            raise TypeError('classname must be a string!')
        if classes.get(classname, None) is None:
            raise TypeError('wrong type!')
        return list(Storage.__store[classname].values())

    def get(self, classname, id_):
        if not classes.get(classname, None):
            raise TypeError('unsupported type "{}"'.format(classname))
        return Storage.__store[classname].get(id_, None)

    def filter(self, classname, **kwargs):
        """filters a set of objects by abitrary key(s)"""
        if type(classname) is not str:
            raise TypeError('classname must be a string!')
        if classname not in classes:
            raise TypeError('Wrong type!')
        # init the filtered list
        filtered = []
        # for each object of the class add those that match
        # the search key to list
        for obj in Storage.__store[classname].values():
            # for each search criteria, if no match skip obj
            matched_flag = 1 # indicates a match of all attrs and value
            for attr, value in kwargs.items():
                if getattr(obj, attr, None) != value:
                    matched_flag = 0
                    break
            if matched_flag:
                filtered.append(obj)
        return filtered

    def add(self, obj):
        """Add to store"""
        if obj is None:
            raise ValueError('Object Cannot be None!')
        classname = obj.__class__.__name__
        if classname not in classes:
            raise TypeError('Wrong type!')
        Storage.__store[classname][obj.id] = obj

    def remove(self, obj):
        """Removes obj from storage"""
        if obj is None:
            raise ValueError('Object Cannot be None!')
        classname = obj.__class__.__name__
        if classname not in classes:
            raise TypeError('Wrong type!')
        Storage.__store[classname].pop(obj.id, None)
        
    def save(self):
        dict_representation = {}
        for classname, data in Storage.__store.items():
            dict_representation[classname] = {}
            for obj_id, obj in data.items():
                dict_representation[classname][obj_id] = obj.to_dict()
        with open(Storage.__filename, 'w', encoding='utf8') as f:
            json.dump(dict_representation, f)

    def reload(self):
        for classname in classes.keys():
            Storage.__store[classname] = {}
        dict_representation = {}
        if os.path.exists(Storage.__filename):
            with open(Storage.__filename, 'r', encoding='utf8') as f:
                dict_representation = json.load(f)
            for classname, data in dict_representation.items():
                for obj_dict in data.values():
                    class_ = classes[classname]
                    obj = class_(**obj_dict)
                    self.add(obj)
