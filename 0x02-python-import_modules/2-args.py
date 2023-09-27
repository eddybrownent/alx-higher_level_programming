#!/usr/bin/python3
if __name__ == "__main__":
    import sys

# "sys.argv" is a special list that stores the arguments.
    arg_c = len(sys.argv) - 1

    if arg_c == 0:
        print("0 arguments.")
    elif arg_c == 1:
        print("1 argument:")
        print("{}: {}".format(arg_c, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_c))

# we go through each argument and print it with a number
        for i in range(arg_c):
            print("{}: {}".format(i+1, sys.argv[i+1]))
