#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_roma = float('inf')

    for char in roman_string:
        if char not in rom_n:
            return 0

        curr_roma = rom_n[char]

        if curr_roma > last_roma:
            num += curr_roma - 2 * last_roma
        else:
            num += curr_roma

        last_roma = curr_roma

    return num
