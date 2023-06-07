#!/usr/bin/python3

class LockedClass:
    __instance__ = ["first_name"]

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        self.__dict__[name] = value
