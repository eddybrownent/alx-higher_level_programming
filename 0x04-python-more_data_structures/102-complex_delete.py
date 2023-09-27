#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())

    for data in keys_list:
        if value == a_dictionary.get(data):
            del a_dictionary[data]
    return a_dictionary
