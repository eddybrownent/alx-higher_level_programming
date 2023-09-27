#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    arg_c = (len(sys.argv) - 1)
    for i in range(arg_c):
        result = result + int(sys.argv[i + 1])
    print(result)
