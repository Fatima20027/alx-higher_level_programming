#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: This method should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
