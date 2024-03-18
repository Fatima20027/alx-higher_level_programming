#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    biggest = my_list[0]
    if length == 0:
        return None
    for i in my_list[1:]:
        if i > biggest:
            biggest = i
    return biggest
