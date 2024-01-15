#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Initialize th square class"""
    def __init__(self, size=0):
        """
        Args:
            size (int): The value of the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """To retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set the value of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Function to print result"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
        if (self.__size == 0):
            print("")
