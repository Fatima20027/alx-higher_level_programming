#!/usr/bin/python3
'''
    Implementing a Geometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator("width", width, self.__width)
        BaseGeometry.integer_validator("height", height, self.__height)

        def area(self):
            return self.__width * self.__height

        def __str__(self):
            """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
