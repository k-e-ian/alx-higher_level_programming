#!/usr/bin/python3
"""defines a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle.
        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
            x (int): x coordinate of the new rectangle
            y (int): y coordinate of the new rectangle
            id (int): id of the new rectangle
        Raises:
            TypeError: if either width and height is not an int
            ValueError: if either width and height is <= zero
            TypeError: if either x or y is not an int
            ValueError: if either x or y is less than zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''set or get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''set or get the height of the rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''set or get x cordinate of rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''set or get y coordinate of the rectangle'''
        return sel.__y
    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TpeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
