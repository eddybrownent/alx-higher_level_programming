#!/usr/bin/python3
"""
This script has a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): list of integers

    Returns:
        int: a peak element from the list
    """
    if not list_of_integers:
        return None

    """
    range of elements to search within
    """
    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        """
        calculates the middle index mid each iteration
        """
        mid = (start + end) // 2

        """
        checks if mid is greater than its adjacent element to the right
        """
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
