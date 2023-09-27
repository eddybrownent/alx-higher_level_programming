#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for tag in names:
        if tag[:2] != "__":
            print(tag)
