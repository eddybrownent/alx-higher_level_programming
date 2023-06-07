#!/usr/bin/python3
def magic_string():
    magic_string.iteration = getattr(magic_string, 'iteration', -1) + 1
    return ("BestSchool, " * magic_string.iteration) + "BestSchool"
