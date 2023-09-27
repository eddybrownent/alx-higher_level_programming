#!/usr/bin/python3
def fizzbuzz():
    for integer in range(1, 101):
        if integer % 3 == 0 and integer % 5 == 0:
            print("FizzBuzz", end=' ')
        elif integer % 3 == 0:
            print("Fizz", end=' ')
        elif integer % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(integer), end=' ')
