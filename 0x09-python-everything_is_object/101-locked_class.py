#!/usr/bin/python3
"""module that contains a LockedClass"""


class LockedClass:
    """
    LockedClass prevents the creation of new instance attributes,
    except for the attribute 'first_name'
    """
    __slots__ = ["first_name"]
