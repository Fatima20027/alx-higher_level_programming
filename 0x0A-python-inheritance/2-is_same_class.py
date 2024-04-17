#!/usr/bin/python3
"""Module: 2-is_same_class.
Check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class name to compare against.

    Returns:
    True if the object is exactly an instance of the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj is a_class)
    #return True if type(obj) is a_class else False