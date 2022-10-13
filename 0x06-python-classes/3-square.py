#!/usr/bin/python3
''' define a class square'''


class Square:
    '''represent a class'''
    def __init__(self, size=0):
        '''initialize a new square

        Args:
            size (int): size of square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''current area squared'''
        return (self.__size * self.__size)
