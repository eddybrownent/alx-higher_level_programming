#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict_ord = list(a_dictionary.keys())
    dict_ord.sort()
    for i in dict_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
