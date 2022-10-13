#!/usr/bin/python3
'''define a class square'''


class Square:
    '''represent square'''
    def __init__(self, size):
        '''initialize square
        Args:
            size (int): size of square
        '''
        self.size = size

    @property
    def size(self):
        '''get square size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''size of area squared'''
        return (self.__size * self.__size)

    def my_print(self):
        '''print square with # char'''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
