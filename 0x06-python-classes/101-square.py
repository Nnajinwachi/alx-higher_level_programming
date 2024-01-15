#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Initialize th square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): The value of the size of the square
            position (tuple): values of position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """To retrieve the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """To set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """To retrieve the positon"""
        return self.__position

    @size.setter
    def position(self, value):
        """To set values of  position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with a character"""
        if self.__size == 0:
            print("")
            return

        [print("") for k in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end='') for k in range(0, self.__position[0])]
            [print("#", end='') for j in range(self.__size)]
            print("")

    def __str__(self):
        """Prints the square with a character"""
        if self.__size != 0:
            [print("") for k in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end='') for k in range(0, self.__position[0])]
            [print("#", end='') for j in range(self.__size)]
            if (self.__size != -1):
                print("")
        return ("")
