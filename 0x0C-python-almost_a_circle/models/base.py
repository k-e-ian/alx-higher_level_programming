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

    @classmethod
    def save_to_file(cls, list_objs):
        '''write the json serialization of list of objects to a file
        Args:
            list_objs (list): a list of inherited base instances
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))
