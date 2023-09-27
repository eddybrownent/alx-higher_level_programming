#!/usr/bin/python3
for digit in range(0, 100):
    if digit == 99:
        print("{}".format(digit), end='\n')
    else:
        print("{:02}".format(digit), end=', ')
