#!/usr/bin/python3
"""defines a base model class"""
import json


class Base:
    """represent the base mode"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new Base
        Args:
            id (int): id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return the JSON serialization of a list of dictionaries
        Args:
            list_dictionaries (list): a list of dictionaries
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
