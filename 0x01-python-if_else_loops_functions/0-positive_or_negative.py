#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > int(0):
    print(f"{number} is positive")
elif number == int(0):
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
