#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list_copy = my_list[:]
        new_list_copy[idx] = element
        return new_list_copy
