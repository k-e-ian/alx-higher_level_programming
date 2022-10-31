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
        else:
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
        else:
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
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

    @property
    def y(self):
        '''set or get y coordinate of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError('y must be >= 0')
            self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def display(self):
        '''print rectangle of hashes'''
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for i in range(self.width)]
            print("")

    def __str__(self):
        '''return the print() and str() representation of rectangle'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """update rectangle
        Args:
            *args (ints): new attribute values
                - arg1 - id attribute
                - arg2 - width attribute
                - arg3 - height attribute
                - arg4 - x attribute
                - arg5 - y attribute
            **kwargs (dict): new key=value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, w in kwargs.items():
                if k == "id":
                    if w is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = w
                elif k == "width":
                    self.width = w
                elif k == "height":
                    self.height = w
                elif k == "x":
                    self.x = w
                elif k == "y":
                    self.y = w
