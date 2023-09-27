#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_int = number % 10
else:
    last_int = ((number * -1) % 10) * -1
if last_int == 0:
    print(f"Last digit of {number} is {last_int} and is 0")
elif last_int > 5:
    print(f"Last digit of {number} is {last_int} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_int} and is less than 6 and not 0")
