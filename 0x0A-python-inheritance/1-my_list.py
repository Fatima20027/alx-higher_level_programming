#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
