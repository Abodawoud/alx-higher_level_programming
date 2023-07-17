#!/usr/bin/python3
"""models/base.py"""
import json

class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON representation of an object (string)"""
        return (json.dumps(list_dictionaries))
