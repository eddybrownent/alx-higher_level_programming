#!/usr/bin/python3
"""module that contains a LockedClass"""


class LockedClass:
    """
    LockedClass prevents the creation of new instance attributes,
    except for the attribute 'first_name'
    """
    __instance__ = ["first_name"]

    def __setattr__(self, name, value):
        """
        Custom attribute method that allow assigning of
        the 'first_name' attribute and raises an error for any
        other attribute assignment.
        """
        msg = "'LockedClass' object has no attribute 'last_name'"
        if name != "first_name":
            raise AttributeError(msg)
        self.__dict__[name] = value
