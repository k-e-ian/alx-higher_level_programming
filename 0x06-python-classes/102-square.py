#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return are of square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define the == comparison of a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != comparison of a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define the < comparison of a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """define the <= comparison of a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define the > comparison of a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define the >= comparison of a square"""
        return self.area() >= other.area()
