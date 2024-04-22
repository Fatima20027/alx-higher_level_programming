#!/usr/bin/python3
'''
    Class Rectangle
'''


from models.base import Base


class Rectangle(Base):
    '''
        Defining the Rectangle class
        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
            Returning private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            Returning private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            Returning private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        '''
            Returns the area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        for row in range(self.__y):
            print("")
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''
            Overwritting the str method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if args and len(args) != 0:
            lst_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                self.__setattr__(lst_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'width': getattr(self, "width"),
                'height': getattr(self, "height"),
                'id': getattr(self, "id")}
