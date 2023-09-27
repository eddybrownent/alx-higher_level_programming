#!/usr/bin/python3

def weight_average(my_list=[]):
    if list and len(my_list):
        nume = 0
        denom = 0
        for tup in my_list:
            nume = nume + (tup[0] * tup[1])
            denom = denom + tup[1]
        return nume/denom
    else:
        return 0
