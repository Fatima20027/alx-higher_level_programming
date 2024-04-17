#!/usr/bin/python3
"""
Module: 6-base_geometry
Public instance method: def area(self): that raises an Exception
with the message
area() is not implemented
"""


class BaseGeometry:
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: This method should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
