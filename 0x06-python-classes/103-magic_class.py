#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by ALX"""

import math


class MagicClass:
    """represent a circle"""

    def __init__(self, radius=0):
        """initialize a circle
        Args:
            radius (int or float): radius of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return area of a circle magicclass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return the circumference of a circle magicclass"""
        return (2 * math.pi * self.__radius)
