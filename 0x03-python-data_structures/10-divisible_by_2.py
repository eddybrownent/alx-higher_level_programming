#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        result = []  # Initialize an empty list to store Boolean values
        for num in my_list:
            result.append(num % 2 == 0)  # Append True if divisible by 2
        return result
    else:
        return None  # Return None for an empty list
