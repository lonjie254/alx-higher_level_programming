#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize width and height """
        self.height = height
        self.width = width

    def __str__(self):
        """ returns set of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]

      @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates and returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates and returns the Rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
