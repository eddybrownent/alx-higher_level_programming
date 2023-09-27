#!/usr/bin/python3
"""
this module has a class that
inherits for the the class List
"""


class MyList(list):
    """
    class that inherits from List
    """
    def print_sorted(self):
        """
        prints the sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
