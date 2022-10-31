#!/usr/bin/python3
"""define a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new square
        Args:
            size (int): size of new square
            x (int): x cootdinate of new square
            y (int): y coordinate of new square
            id (int): identity of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''get the size of square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        '''return the dictionary represantion of square'''
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        '''return the print() and str() representation of a square'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''update the square
        Args:
            *args (ints): new attribute values
                - arg1 - id attribute
                - arg2 - size attribute
                - arg3 - x attribute
                - arg4 - y attribute
            **kwargs (dict): New key=value pairs of attribute
        '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, w in kwargs.items():
                if k == "id":
                    if w is None:
                        self.__init__(self.sizw, self.x, self.y)
                    else:
                        self.id = w
                elif k == "size":
                    self.size = w
                elif k == "x":
                    self.x = w
                elif k == "y":
                    self.y = w
